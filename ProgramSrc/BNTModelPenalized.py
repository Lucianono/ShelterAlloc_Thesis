# the official function for Bilevel No Transfer model

from PySide6.QtCore import QObject, Signal
from DataSetsModel import DataSets
import random
import numpy as np
import copy
import time
from datetime import datetime
import pandas as pd
import os

import uuid
import socket
import requests
import sys

class BNTModelSimulation(QObject):

    finished = Signal()
    progress_msg = Signal(str)
    
    def cancel(self):
        self.cancelled = True

    def progress_dialog(self,msg):
        self.progress_msg.emit(msg)
    
    def run(self):
        try :
            self.run_algo()
        finally :
            self.finished.emit()

    def run_algo(self):

        self.progress_dialog("Starting simulation")
        print("Starting simulation")
        self.cancelled = False
        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")

        datasets = DataSets()
        Community = datasets.get_community_data()
        Shelters = datasets.get_shelter_data()

        Model_parameters = pd.read_excel( os.path.join(self.save_dir, "modelParam.xlsx"), header=0 ).iloc[0]
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
                print("max shelters constraint failed")
                penalty += len(used_shelters) - max_shelters
                    
            return penalty
                
        # max lvl2 shelters to be constructed/allocated constraint (2.26)
        def check_max_lvl2_shelters(allocation):
            
            lvl2_shelters_ctr = sum(1 for level in allocation["shelterlvl"].values() if level == 2)
            penalty = 0

            if lvl2_shelters_ctr > max_lvl2_shelters:
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
                self.progress_dialog(f"Shelter: {shelter} (Level {details['level']})")
                print(f"Shelter: {shelter} (Level {details['level']})")
                self.progress_dialog(f"  Initial:")
                print(f"  Initial:")
                for community in details['initial']:
                    self.progress_dialog(f"    - {community}")
                    print(f"    - {community}")
                print()

        
        def export_to_excel(allocation):
            data = []
            
            for community in Community:
                shelter_name = allocation["initial"][community["name"]]
                
                # Append data
                data.append({
                    "Community": community["name"],
                    "Allocated Population": community["population"],
                    "Shelter Assigned": shelter_name,
                    "Level": allocation["shelterlvl"][shelter_name]
                })
            
            # Create a DataFrame and export to Excel
            df = pd.DataFrame(data)
            output_file = os.path.join(self.save_dir, "allocation_results.xlsx")
            df.to_excel(output_file, index=False)

            self.progress_dialog(f"Allocation results saved to {output_file}")
            print(f"Allocation results saved to {output_file}")



        # =======================
        # START OF THE ALGORITHM
        # initial population

        generation_last_updated = 0

        for _ in range(num_solutions):
            solution = spawn()
            solutions.append(solution)

        # generations
        for generation in range(num_generations):
            # check for cancellation
            if self.cancelled:
                self.progress_dialog("Genetic algorithm cancelled.")
                return

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

            if (generation+1) % 100 == 0 :
                self.progress_dialog(str(best_solutions[0]))
                print(best_solutions[0])
                self.progress_dialog(f"=== Gen {generation+1} best solution ===")
                print(f"=== Gen {generation+1} best solution ===")

            prev_best_solution = fitness(solutions[0])

            # replace old population
            solutions = [sol[1] for sol in best_solutions]

            new_best_solution = fitness(solutions[0])

            #update generation_last_updated
            if(prev_best_solution != new_best_solution):
                generation_last_updated = generation+1

        
        self.progress_dialog(str(best_solutions[0]))
        print(best_solutions[0])
        self.progress_dialog(f"=== Gen {generation+1} best solution ===")
        print(f"=== Gen {generation+1} best solution ===")
        best_allocation = solutions[0]
        show_allocation_details_grouped(best_allocation)
        self.progress_dialog(f"Generation when solution last updated : {generation_last_updated}")
        print(f"Generation when solution last updated : {generation_last_updated}")

        export_to_excel(best_allocation)

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Convert to minutes and seconds
        minutes = int(elapsed_time // 60)
        seconds = elapsed_time % 60

        self.progress_dialog(f"--- {minutes} minutes and {seconds:.2f} seconds ---")
        print(f"--- {minutes} minutes and {seconds:.2f} seconds ---")

        # =======================
        # DETAILS RECORDING
        def cost_of_open_shelter(allocation):

            initial_shelters = set(allocation['initial'].values())
            Shelters_dict = {shelter["name"]: shelter for shelter in Shelters}

            total_cost = 0

            for shelter_name in initial_shelters:
                # add cost based on shelter level
                shelter = Shelters_dict.get(shelter_name)
                if (allocation["shelterlvl"][shelter_name] == 1):
                    total_cost += shelter["cost1"] 
                elif (allocation["shelterlvl"][shelter_name] == 2):
                    total_cost += shelter["cost2"] 
                else:
                    self.progress_dialog("Shelter exceeded 2 levels. Something is wrong")
                    print("Shelter exceeded 2 levels. Something is wrong")

            return int(total_cost)
        
        def cost_of_all_lvl1_shelter():

            total_cost = sum(shelter["cost1"] for shelter in Shelters)

            return int(total_cost)
        
        # Cost rate generator
        #new-old / old
        cost_comparison_analysis = "-"
        if cost_of_all_lvl1_shelter() > 0:
            cost_diff_rate = (cost_of_open_shelter(best_allocation) - cost_of_all_lvl1_shelter()) / cost_of_all_lvl1_shelter()
            if cost_diff_rate < 0:    
                cost_comparison_analysis = f"Cost saved by {abs(cost_diff_rate):.2%}"
            elif cost_diff_rate > 0:  
                cost_comparison_analysis = f"Cost increased by {cost_diff_rate:.2%}"

        # pc details
        mac_address = ':'.join(format(b, '02x') for b in uuid.getnode().to_bytes(6, 'big'))
        username = os.getlogin()
        local_ip = socket.gethostbyname(socket.gethostname())
        try:
            public_ip = requests.get("https://api64.ipify.org").text
        except requests.RequestException:
            public_ip = "Unavailable"
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to a txt file
        data = [
            f"Generation when solution last updated : {generation_last_updated}",
            f"Time run : {minutes} minutes and {seconds:.2f} seconds",
            cost_comparison_analysis,
            f"Objective value : {fitness(best_allocation)}",
            "--- SHELTER DETAILS ---",
            f"Number of all shelters : {sum(1 for shelter in Shelters)}",
            f"Number of opened shelters : {sum(1 for shelter in set(best_allocation['initial'].values()))}",
            f"Cost of all level 1 shelters : {cost_of_all_lvl1_shelter()}",
            f"Cost of opened shelters : {cost_of_open_shelter(best_allocation)}",
            "--- GENETIC ALGORITHM PARAMETERS ---",
            f"Number of generations : {num_generations}",
            f"Number of population per generation : {num_solutions}",
            f"Mutation rate : {mutation_rate}",
            "--- MODEL PARAMETERS ---",
            f"Weight of Distance : {weight_dist}",
            f"Weight of Cost : {weight_cost}",
            f"Area per Individual : {area_per_individual}",
            f"Set number of max shelters : {max_shelters}",
            f"Set number of max level 2 shelters : {max_lvl2_shelters}",
            "--- REPORT and USER DETAILS ---",
            f"MAC Address : {mac_address}",
            f"PC Username : {username}",
            f"Local IP Address : {local_ip}",
            f"Public IP Address : {public_ip}",
            f"Time of report generation : {date_now}",
        ]

        with open( os.path.join(self.save_dir, "modelPerformanceResult.txt"), "w") as file:
            # Write each line to the file
            for line in data:
                file.write(line + "\n")  # Add a newline character after each line