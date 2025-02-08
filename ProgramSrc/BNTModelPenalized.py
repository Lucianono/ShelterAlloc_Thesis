# the official function for Bilevel No Transfer model

from DataSetsModel import DataSets
import random
import numpy as np
import copy
import time
import pandas as pd
import os

class BNTModelSimulation:
    
    def run(self, progress_dialog):
        # TEMPORARY DUMMY DATA
        # should be replaced with dynamic data from system
        # simulation of area required per individual (meters squared), maximum no. of level 2 shelters
        progress_dialog("Starting simulation")
        print("Starting simulation")

        datasets = DataSets()
        Community = datasets.get_community_data()
        Shelters = datasets.get_shelter_data()

        Model_parameters = pd.read_excel( os.path.join(os.getcwd(), "modelParam.xlsx"), header=0 ).iloc[0]
        area_per_individual = Model_parameters['AreaPerIndiv']
        max_lvl2_shelters = int(min(Model_parameters['MaxL2Shelters'], len(Shelters)))
        max_shelters = int(min(Model_parameters['MaxShelters'], len(Shelters)))

        solutions = []
        num_generations = int(Model_parameters['Generations'])
        num_solutions = int(Model_parameters['Population'])
        mutation_rate = Model_parameters['Mutation']
        mutation_iteration = 2

        weight_dist = Model_parameters['WtDist']
        weight_cost = Model_parameters['WtCost']
        penalty_constant = 10**20

        start_time = time.time()

        # =======================
        # SOLUTION SPAWNING
        # create chromosome with randomized allocation
        def spawn():
            allocations = {}
            shelter_lvl_assignment = {}

            for community in Community:
                shelter = random.choice(Shelters)["name"]
                allocations[community["name"]] = shelter

            for shelter in Shelters:
                level = random.choice([1,2])
                shelter_lvl_assignment[shelter["name"]] = level

            allocations = {"initial": allocations, "shelterlvl": shelter_lvl_assignment}
            return allocations

        # =======================
        # OBJECTIVE FUNCTION
        # also the fitness
        # minimize fitness
        def fitness(allocation):

            initial_shelters = set(allocation['initial'].values())
            Shelters_dict = {shelter["name"]: shelter for shelter in Shelters}

            total_distance = 0
            total_cost = 0

            for community in Community:
                # add distance * population
                shelter_name = allocation["initial"][community["name"]]
                distance = community["distances"][shelter_name]
                total_distance += distance * community["population"]


            for shelter_name in initial_shelters:
                # add cost based on shelter level
                shelter = Shelters_dict.get(shelter_name)
                if (allocation["shelterlvl"][shelter_name] == 1):
                    total_cost += shelter["cost1"] 
                elif (allocation["shelterlvl"][shelter_name] == 2):
                    total_cost += shelter["cost2"] 
                else:
                    progress_dialog("Shelter exceeded 2 levels. Something is wrong")
                    print("Shelter exceeded 2 levels. Something is wrong")
                
            # the actual model
            objective_value = weight_dist * total_distance + weight_cost * total_cost
            penalty_value = penalty_constant * getPenaltySum(allocation)

            # handle division by zero
            if objective_value + penalty_value == 0:
                return 1

            return int(objective_value + penalty_value)

        # =======================
        # CONSTRAINTS
        # maximum distance constraint (2.24)
        def check_max_distance(allocation):

            penalty = 0

            for community in Community:
                shelter_name = allocation["initial"][community["name"]]
                distance = community["distances"][shelter_name]
                max_distance_community = community["maxdistance"]
                # check if distance is greater than max dist
                if (distance > max_distance_community):
                    progress_dialog("maximum distance constraint failed")
                    print("maximum distance constraint failed")
                    penalty += distance - max_distance_community
                
            return penalty

        # initial capacity constraint (2.25)
        def check_initial_capacity(allocation):
            shelter_areas = {shelter["name"]: shelter[f"area{allocation["shelterlvl"][shelter['name']]}"] for shelter in Shelters}
            used_area = {shelter["name"]: 0 for shelter in Shelters}

            penalty = 0

            for community in Community:
                shelter_name = allocation["initial"][community["name"]]
                if shelter_name:
                    # add to used_area based on population
                    required_area = community["population"] * area_per_individual
                    used_area[shelter_name] += required_area

                    if used_area[shelter_name] > shelter_areas[shelter_name]:
                        progress_dialog("initial capacity constraint failed")
                        print("initial capacity constraint failed")

            for shelter in Shelters:
                shelter_name = shelter["name"]
                penalty_value = used_area[shelter_name] - shelter_areas[shelter_name]
                penalty += max(0,penalty_value)

            return penalty

        # max shelters to be constructed/allocated constraint (2.27)
        def check_max_shelters(allocation):
            used_shelters = set() 
            penalty = 0

            for community in Community:
                shelter_name = allocation["initial"][community["name"]]
                used_shelters.add(shelter_name)  

            # If the number of unique shelters exceeds the max allowed
            if len(used_shelters) > max_shelters:
                progress_dialog("max shelters constraint failed")
                print("max shelters constraint failed")
                penalty += len(used_shelters) - max_shelters
                    
            return penalty
                
        # max lvl2 shelters to be constructed/allocated constraint (2.26)
        def check_max_lvl2_shelters(allocation):
            
            lvl2_shelters_ctr = sum(1 for level in allocation["shelterlvl"].values() if level == 2)
            penalty = 0

            if lvl2_shelters_ctr > max_lvl2_shelters:
                progress_dialog("max lvl2 shelters constraint failed")
                print("max lvl2 shelters constraint failed")
                penalty += lvl2_shelters_ctr - max_lvl2_shelters 
        
            return penalty

        # =======================
        # CONSTRAINTS/PENALTY EXECUTION
        # Check all constraints
        def getPenaltySum(allocation):
            return (check_initial_capacity(allocation)**2 +  
                    check_max_distance(allocation)**2 + 
                    check_max_shelters(allocation)**2 + 
                    check_max_lvl2_shelters(allocation)**2 )

        # =======================
        # GENETIC ALGORITHM
        # mutation operator
        # TYPE : Random Reset
        def mutate(allocation):
            new_allocations = copy.deepcopy(allocation)

            for _ in range(mutation_iteration) : 
                key_rand = random.choice(list(allocation.keys()))
                gene_to_mutate = random.choice(list(allocation[key_rand].keys()))
                current_value = allocation[key_rand][gene_to_mutate]
                
                if key_rand == "initial" or key_rand == "transferred":
                    available_choices = [shelter["name"] for shelter in Shelters if shelter["name"] != current_value]
                elif key_rand == "shelterlvl":
                    available_choices = [1,2]
                    available_choices.remove(current_value)

                if available_choices:
                    new_value = random.choice(available_choices)
                    new_allocations[key_rand][gene_to_mutate] = new_value
                    
            return new_allocations


        # crossover operator
        # TYPE : Uniform Crossover
        def generate_offspring(parent1, parent2):
            offspring = {"initial":{},"shelterlvl":{}}
            for community in Community:
                #for initial
                shelters = {parent1["initial"][community["name"]], parent2["initial"][community["name"]]} 
                
                if shelters:
                    chosen_shelter = random.choice(list(shelters))
                else:
                    chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

                offspring["initial"][community["name"]] = chosen_shelter

            for shelter in Shelters:

                #for shelterlvl
                levels = {parent1["shelterlvl"][shelter["name"]], parent2["shelterlvl"][shelter["name"]]} 
                
                if shelters:
                    chosen_lvl = random.choice(list(levels))
                else:
                    chosen_lvl = random.choice([1,2])

                offspring["shelterlvl"][shelter["name"]] = chosen_lvl

            return offspring

        # selection operator
        # TYPE : Roulette Wheel Selection
        def selectParent(solutions):
            sum_fitness = sum(fitness for fitness, _ in solutions)
            inv_proportions = [sum_fitness/ fitness for fitness, _ in solutions]
            sum_inv_proportions = sum(inv_proportions)
            probability = [inv_proportion / sum_inv_proportions for inv_proportion in inv_proportions]
            solution_indices = np.arange(len(solutions))

            selected_solution = np.random.choice(solution_indices, p=probability)

            return solutions[selected_solution]

        # =======================
        # FEASIBILITY CHECK
        # check if data input has solution
        def feasibilityCheck():
            # check if there exists distance <= max distance 
            failing_communities = []
            for community in Community:
                if not any(d <= community["maxdistance"] for d in community["distances"].values()):
                    failing_communities.append(community["name"])
            
            if failing_communities:
                progress_dialog(f"{failing_communities} has maximum distance that is impossible to allocate. No shelters is close enough.")
                print(f"{failing_communities} has maximum distance that is impossible to allocate. No shelters is close enough.")
                return False

            # check if there exists population <= shelter area * areaPerIndiv
            failing_communities = []
            for community in Community:
                if not (
                    any(shelter["area1"] * area_per_individual >= community["population"] for shelter in Shelters) or
                    any(shelter["area2"] * area_per_individual >= community["population"] for shelter in Shelters)
                ):
                    failing_communities.append(community["name"])
            
            if failing_communities:
                progress_dialog(f"{failing_communities} has affected population that is impossible to allocate. No shelters is large enough.")
                print(f"{failing_communities} has affected population that is impossible to allocate. No shelters is large enough.")
                return False

            # check if total population is theoretically possible to allocate on largest  shelters
            total_population = sum(community['population'] for community in Community)

            Shelters_sorted = sorted(Shelters, key=lambda x: x['area2'], reverse=True)
            top_area2_sum = sum(shelter['area2'] for shelter in Shelters[:max_lvl2_shelters])
            Shelters_sorted = Shelters_sorted[max_lvl2_shelters:]

            Shelters_sorted = sorted(Shelters, key=lambda x: x['area1'], reverse=True)
            top_area1_sum = sum(shelter['area1'] for shelter in Shelters[:(max_shelters - max_lvl2_shelters)])
            Shelters_sorted = Shelters_sorted[(max_shelters - max_lvl2_shelters):]

            if total_population > (top_area2_sum + top_area1_sum):
                progress_dialog(f"Total capacity of shelters available are less than the total affected population. Shelters has lower than expected capacity")
                print(f"Total capacity of shelters available are less than the total affected population. Shelters has lower than expected capacity")
                return False
            
            # if no cases are violated return true
            return True

        # =======================
        # LOGIC CHECK
        # check if parameters are logical or correct
        def logicCheck():
            # check if max_shelters >= max_lvl2_shelters
            if max_shelters < max_lvl2_shelters:
                progress_dialog("max_shelters should be greater than or equal to max_lvl2_shelters")
                print("max_shelters should be greater than or equal to max_lvl2_shelters")
                return False
            # check if max_shelters >= 1
            if max_shelters < 1:
                progress_dialog("max_shelters should have atleast 1")
                print("max_shelters should have atleast 1")
                return False
            # check if area_per_individual > 0
            if area_per_individual <= 0:
                progress_dialog("area_per_individual should be greater than 0")
                print("area_per_individual should be greater than 0")
                return False
            # check if num_generations >= 1
            if num_generations < 1:
                progress_dialog("num_generations should be greater than or equal to 1")
                print("num_generations should be greater than or equal to 1")
                return False
            # check if num_solutions >= 1
            if num_solutions < 1:
                progress_dialog("num_solutions should be greater than or equal to 1")
                print("num_solutions should be greater than or equal to 1")
                return False
            # check if mutation_rate not < 0
            if mutation_rate < 0:
                progress_dialog("mutation_rate should not be less than to 0")
                print("mutation_rate should not be less than to 0")
                return False
            # check if weight_dist not < 0
            if weight_dist < 0:
                progress_dialog("weight_dist should not be less than to 0")
                print("weight_dist should not be less than to 0")
                return False
            # check if weight_cost not < 0
            if weight_cost < 0:
                progress_dialog("weight_cost should not be less than to 0")
                print("weight_cost should not be less than to 0")
                return False
            # check if area2 >= area1
            for shelter in Shelters:
                if shelter["area2"] < shelter["area1"]:
                    progress_dialog(f"{shelter['name']}: area2 should be grated than or equal to area1.")
                    print(f"{shelter['name']}: area2 should be grated than or equal to area1.")
                    return False


            # if no cases are violated return true
            return True

        # =======================
        # DISPLAY ALLOCATION
        def show_allocation_details_grouped(allocation):
            # Grouping communities by shelters for initial allocations
            grouped_by_shelter = {}

            for phase, allocations in allocation.items():
                if phase in ('initial'):
                    for community, shelter in allocations.items():
                        if shelter not in grouped_by_shelter:
                            grouped_by_shelter[shelter] = {'level': allocation['shelterlvl'].get(shelter, None), 'initial': []}
                        grouped_by_shelter[shelter][phase].append(community)

            # Print the grouped data
            for shelter, details in grouped_by_shelter.items():
                progress_dialog(f"Shelter: {shelter} (Level {details['level']})")
                print(f"Shelter: {shelter} (Level {details['level']})")
                progress_dialog(f"  Initial:")
                print(f"  Initial:")
                for community in details['initial']:
                    progress_dialog(f"    - {community}")
                    print(f"    - {community}")
                print()

        
        def export_to_excel(allocation):
            data = []
            
            for community in Community:
                shelter_name = allocation["initial"][community["name"]]
                
                # Append data
                data.append({
                    "Community Name": community["name"],
                    "Shelter Assigned": shelter_name,
                    "Shelter Level": allocation["shelterlvl"][shelter_name]
                })
            
            # Create a DataFrame and export to Excel
            df = pd.DataFrame(data)
            output_file = os.path.join(os.getcwd(), "allocation_results.xlsx")
            df.to_excel(output_file, index=False)

            progress_dialog(f"Allocation results saved to {output_file}")
            print(f"Allocation results saved to {output_file}")

        # =======================
        # START OF THE ALGORITHM
        # initial population
        if not logicCheck():
            progress_dialog("Parameters are inputted incorrectly.")
            print("Parameters are inputted incorrectly.")
            exit()
        if not feasibilityCheck():
            progress_dialog("No solution exists")
            print("No solution exists")
            exit()

        infeasibility_ctr = 0
        generation_last_updated = 0

        for _ in range(num_solutions):
            solution = spawn()


            fitnessVal = fitness(solution)
            solutions.append(solution)
            infeasibility_ctr = 0

        # generations
        for generation in range(num_generations):

            # sorting from best to worst solutions
            ranked_solutions = [(fitness(sol), sol) for sol in solutions]
            ranked_solutions.sort(key=lambda x: x[0])

            # initiate selection and crossover
            new_population = []
            for i in range(num_solutions):
                mother = selectParent(ranked_solutions)[1]
                father = selectParent(ranked_solutions)[1]

                offspring = generate_offspring(mother, father)
                new_population.append(offspring)

            # initiate mutation
            mutated_population = []
            for solution in new_population:
                if random.random() < mutation_rate:
                    solution = mutate(solution)
                mutated_population.append((fitness(solution),solution))

            # getting the top half solutions
            best_solutions = mutated_population + ranked_solutions
            best_solutions = sorted(best_solutions, key=lambda x: x[0])[:num_solutions] 

            progress_dialog(f"=== Gen {generation+1} best solution ===")
            print(f"=== Gen {generation+1} best solution ===")
            progress_dialog(str(best_solutions[0]))
            print(best_solutions[0])

            prev_best_solution = fitness(solutions[0])

            # replace old population
            solutions = [sol[1] for sol in best_solutions]

            new_best_solution = fitness(solutions[0])

            #update generation_last_updated
            if(prev_best_solution != new_best_solution):
                generation_last_updated = generation+1


        best_allocation = solutions[0]
        show_allocation_details_grouped(best_allocation)
        progress_dialog(f"Generation when solution last updated : {generation_last_updated}")
        print(f"Generation when solution last updated : {generation_last_updated}")

        export_to_excel(best_allocation)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Convert to minutes and seconds
        minutes = int(elapsed_time // 60)
        seconds = elapsed_time % 60

        progress_dialog(f"--- {minutes} minutes and {seconds:.2f} seconds ---")
        print(f"--- {minutes} minutes and {seconds:.2f} seconds ---")

        data = [
            f"Number of generations : {num_generations}",
            f"Number of population per generation : {num_solutions}",
            f"Mutation rate : {mutation_rate}",
            f"Weight of Distance : {weight_dist}",
            f"Weight of Cost : {weight_cost}",
            f"Area per Individual : {area_per_individual}",
            f"Set number of max shelters : {max_shelters}",
            f"Set number of max level 2 shelters : {max_lvl2_shelters}",
            f"Generation when solution last updated : {generation_last_updated}",
            f"Time run : {minutes} minutes and {seconds:.2f} seconds"
        ]

        # Open a file in write mode ('w')
        with open("modelPerformanceResult.txt", "w") as file:
            # Write each line to the file
            for line in data:
                file.write(line + "\n")  # Add a newline character after each line