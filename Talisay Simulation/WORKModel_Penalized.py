from Talisay_Data_Modified import Community, Shelters
import random
import numpy as np
import copy
import time


class WORKModel:

    def __init__(self):
        self.area_per_individual = 1
        self.max_lvl2_shelters = 33
        self.max_shelters = 33

        self.num_generations = 10000
        self.num_solutions = 100
        self.mutation_rate = 0.8
        self.mutation_iteration = 2

        self.weight_dist = 0.3
        self.weight_cost = 0.3
        self.weight_work = 0.4
        self.penalty_constant = 10**20

        self.solutions = []
        self.generation_last_updated = 0
        self.generations_updated_arr = [0]
        self.obj_value_updated_arr = []

    # =======================
    # SOLUTION SPAWNING
    def spawn(self):
        allocations = {}
        for community in Community:
            shelter = random.choice(Shelters)["name"]
            allocations[community["name"]] = shelter
        return {"initial": allocations}

    # =======================
    # OBJECTIVE FUNCTION
    def fitness(self, allocation):
        initial_shelters = set(allocation['initial'].values())
        Shelters_dict = {shelter["name"]: shelter for shelter in Shelters}

        total_distance = 0
        total_workdistance = 0
        total_cost = 0

        for community in Community:
            shelter_name = allocation["initial"][community["name"]]
            distance = community["distances"][shelter_name]
            total_distance += distance * community["population"]

            for work in community["portionwork"]:
                workdistance = Shelters_dict.get(shelter_name)["distanceswork"][work]
                total_workdistance += workdistance * community["portionwork"][work] * community["population"]

        for shelter_name in initial_shelters:
            shelter = Shelters_dict.get(shelter_name)
            total_cost += shelter["cost1"]

        objective_value = self.weight_dist * total_distance + self.weight_work * total_workdistance + self.weight_cost * total_cost
        penalty_value = self.penalty_constant * self.getPenaltySum(allocation)

        return int(objective_value + penalty_value)

    # =======================
    # CONSTRAINTS
    def check_max_distance(self, allocation):
        penalty = 0
        for community in Community:
            shelter_name = allocation["initial"][community["name"]]
            distance = community["distances"][shelter_name]
            max_distance_community = community["maxdistance"]
            if distance > max_distance_community:
                penalty += distance - max_distance_community
        return penalty

    def check_initial_capacity(self, allocation):
        shelter_areas = {shelter["name"]: shelter["area1"] for shelter in Shelters}
        used_area = {shelter["name"]: 0 for shelter in Shelters}
        penalty = 0

        for community in Community:
            shelter_name = allocation["initial"][community["name"]]
            if shelter_name:
                required_area = community["population"] * self.area_per_individual
                used_area[shelter_name] += required_area

        for shelter in Shelters:
            shelter_name = shelter["name"]
            penalty_value = used_area[shelter_name] - shelter_areas[shelter_name]
            penalty += max(0, penalty_value)

        return penalty

    def check_max_shelters(self, allocation):
        used_shelters = set()
        for community in Community:
            shelter_name = allocation["initial"][community["name"]]
            used_shelters.add(shelter_name)

        penalty = 0
        if len(used_shelters) > self.max_shelters:
            penalty += len(used_shelters) - self.max_shelters
        return penalty

    def getPenaltySum(self, allocation):
        return (self.check_initial_capacity(allocation)**2 +
                self.check_max_distance(allocation)**2 +
                self.check_max_shelters(allocation)**2)

    # =======================
    # GENETIC OPERATORS
    def mutate(self, allocation):
        new_allocations = copy.deepcopy(allocation)

        for _ in range(self.mutation_iteration):
            key_rand = random.choice(list(allocation.keys()))
            gene_to_mutate = random.choice(list(allocation[key_rand].keys()))
            current_value = allocation[key_rand][gene_to_mutate]

            if key_rand in ("initial", "transferred"):
                available_choices = [shelter["name"] for shelter in Shelters if shelter["name"] != current_value]
            elif key_rand == "shelterlvl":
                available_choices = [1, 2]
                available_choices.remove(current_value)

            if available_choices:
                new_allocations[key_rand][gene_to_mutate] = random.choice(available_choices)

        return new_allocations

    def generate_offspring(self, parent1, parent2):
        offspring = {"initial": {}}
        for community in Community:
            shelters = {parent1["initial"][community["name"]], parent2["initial"][community["name"]]}
            chosen_shelter = random.choice(list(shelters)) if shelters else random.choice([s["name"] for s in Shelters])
            offspring["initial"][community["name"]] = chosen_shelter
        return offspring

    def selectParent(self, solutions):
        sum_fitness = sum(f for f, _ in solutions)
        inv_proportions = [sum_fitness / f for f, _ in solutions]
        sum_inv = sum(inv_proportions)
        probability = [v / sum_inv for v in inv_proportions]
        selected = np.random.choice(np.arange(len(solutions)), p=probability)
        return solutions[selected]

    # =======================
    # FEASIBILITY / LOGIC CHECKS
    def feasibilityCheck(self):
        failing = [c["name"] for c in Community
                   if not any(d <= c["maxdistance"] for d in c["distances"].values())]
        if failing:
            print(f"{failing} has maximum distance that is impossible to allocate.")
            return False

        failing = [c["name"] for c in Community
                   if not (any(s["area1"] * self.area_per_individual >= c["population"] for s in Shelters) or
                           any(s["area2"] * self.area_per_individual >= c["population"] for s in Shelters))]
        if failing:
            print(f"{failing} has affected population that is impossible to allocate.")
            return False

        total_population = sum(c["population"] for c in Community)

        Shelters_sorted = sorted(Shelters, key=lambda x: x['area2'], reverse=True)
        top_area2_sum = sum(shelter['area2'] for shelter in Shelters[:self.max_lvl2_shelters])
        Shelters_sorted = Shelters_sorted[self.max_lvl2_shelters:]

        Shelters_sorted = sorted(Shelters, key=lambda x: x['area1'], reverse=True)
        top_area1_sum = sum(shelter['area1'] for shelter in Shelters[:(self.max_shelters - self.max_lvl2_shelters)])
        Shelters_sorted = Shelters_sorted[(self.max_shelters - self.max_lvl2_shelters):]

        if total_population > (top_area2_sum + top_area1_sum):
            print(f"Total capacity of shelters available are less than the total affected population. Shelters has lower than expected capacity")
            return False

        return True

    def logicCheck(self):
        if self.max_shelters < self.max_lvl2_shelters:
            print("max_shelters should be >= max_lvl2_shelters")
            return False
        if self.max_shelters < 1:
            print("max_shelters should have at least 1")
            return False
        if self.area_per_individual <= 0:
            print("area_per_individual should be > 0")
            return False
        if self.num_generations < 1:
            print("num_generations should be >= 1")
            return False
        if self.num_solutions < 1:
            print("num_solutions should be >= 1")
            return False
        if self.mutation_rate < 0:
            print("mutation_rate should not be < 0")
            return False
        if self.weight_dist < 0:
            print("weight_dist should not be < 0")
            return False
        if self.weight_cost < 0:
            print("weight_cost should not be < 0")
            return False
        for shelter in Shelters:
            if shelter["area2"] < shelter["area1"]:
                print(f"{shelter['name']}: area2 should be >= area1.")
                return False

        # if no cases are violated return true
        return True

    # =======================
    # DISPLAY
    def show_allocation_details_grouped(self, allocation):
        grouped_by_shelter = {}
        for phase, allocations in allocation.items():
            if phase == "initial":
                for community, shelter in allocations.items():
                    if shelter not in grouped_by_shelter:
                        grouped_by_shelter[shelter] = {"initial": []}
                    grouped_by_shelter[shelter][phase].append(community)

        for shelter, details in grouped_by_shelter.items():
            print(f"Shelter: {shelter}")
            print(f"  Initial:")
            for community in details["initial"]:
                print(f"    - {community}")
            print()

    # =======================
    # MAIN ENTRY POINT
    def start_model(self):
        if not self.logicCheck():
            print("Parameters are inputted incorrectly.")
            return None
        if not self.feasibilityCheck():
            print("No solution exists.")
            return None

        # reset state
        self.solutions = []
        self.generation_last_updated = 0
        self.generations_updated_arr = [0]
        self.obj_value_updated_arr = []
        start_time = time.time()

        # initial population
        for _ in range(self.num_solutions):
            self.solutions.append(self.spawn())

        # generations
        for generation in range(self.num_generations):
            ranked_solutions = [(self.fitness(sol), sol) for sol in self.solutions]
            ranked_solutions.sort(key=lambda x: x[0])

            new_population = []
            for _ in range(self.num_solutions):
                mother = self.selectParent(ranked_solutions)[1]
                father = self.selectParent(ranked_solutions)[1]
                new_population.append(self.generate_offspring(mother, father))

            mutated_population = []
            for solution in new_population:
                if random.random() < self.mutation_rate:
                    solution = self.mutate(solution)
                mutated_population.append((self.fitness(solution), solution))

            best_solutions = sorted(mutated_population + ranked_solutions, key=lambda x: x[0])[:self.num_solutions]

            if (generation + 1) % 100 == 0:
                print(best_solutions[0])
                print(f"=== Gen {generation+1} best solution ===")

            prev_best = self.fitness(self.solutions[0])
            self.solutions = [sol[1] for sol in best_solutions]
            new_best = self.fitness(self.solutions[0])

            if len(self.obj_value_updated_arr) == 0:
                self.obj_value_updated_arr.append(prev_best)

            if prev_best != new_best:
                self.generation_last_updated = generation + 1
                self.generations_updated_arr.append(self.generation_last_updated)
                self.obj_value_updated_arr.append(new_best)

        best_allocation = self.solutions[0]
        self.show_allocation_details_grouped(best_allocation)

        self.generations_updated_arr.append(self.num_generations)
        self.obj_value_updated_arr.append(self.fitness(best_allocation))

        elapsed = time.time() - start_time
        minutes = int(elapsed // 60)
        seconds = elapsed % 60
        runtime_str = f"{minutes}m {seconds:.2f}s"

        print(f"Generation when solution last updated: {self.generation_last_updated}")
        print(f"--- {runtime_str} ---")

        return {
            "fitness": self.fitness(best_allocation),
            "gen_last_updated": self.generation_last_updated,
            "runtime": runtime_str,
            "runtime_seconds": elapsed,
            "allocation": best_allocation,
        }

    # =======================
    # PLOT
    def plot_graph(self):
        import matplotlib.pyplot as plt
        plt.plot(self.generations_updated_arr, self.obj_value_updated_arr)
        plt.xlabel("Generation")
        plt.ylabel("Objective Value")
        plt.yscale("log")
        plt.xscale("log")
        plt.title("WORK Model")
        plt.show()