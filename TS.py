import pandas as pd
import random as rd
from itertools import combinations
import math

class TS():
    def __init__(self, Path, seed, tabu_tenure):
        self.Path = Path
        self.seed = seed
        self.tabu_tenure = tabu_tenure
        self.instance_dict = self.input_data()
        self.Initial_solution = self.get_InitialSolution()


    def input_data(self):
        '''Takes the path of the excel file of the SMTWTP instances.
        Returns a dict of jobs number as Key and weight, processing time (hours) and due date (hours) as values.
        '''
        return pd.read_excel(self.Path, names=['Job', 'weight', "processing_time", "due_date"],
                                 index_col=0).to_dict('index')

    def get_tabuestructure(self):
        '''Takes a dict (input data)
        Returns a dict of tabu attributes(pair of jobs that are swapped) as keys and [tabu_time, MoveValue]
        '''
        dict = {}
        for swap in combinations(self.instance_dict.keys(), 2):
            dict[swap] = {'tabu_time': 0, 'MoveValue': 0}
        return dict

    def get_InitialSolution(self, show=False):
        n_jobs = len(self.instance_dict) # Number of jobs
        # Producing a random schedule of jobs
        initial_solution = list(range(1, n_jobs+1))
        rd.seed(self.seed)
        rd.shuffle(initial_solution)
        if show == True:
            print("initial Random Solution: {}".format(initial_solution))
        return initial_solution

    def Objfun(self, solution, show = False):
        '''Takes a set of scheduled jobs, dict (input data)
        Return the objective function value of the solution
        '''
        dict = self.instance_dict
        t = 0   #starting time
        objfun_value = 0
        for job in solution:
            C_i = t + dict[job]["processing_time"]  # Completion time
            d_i = dict[job]["due_date"]   # due date of the job
            T_i = max(0, C_i - d_i)    #tardiness for the job
            W_i = dict[job]["weight"]  # job's weight

            objfun_value +=  W_i * T_i
            t = C_i
        if show == True:
            print("\n","#"*8, "The Objective function value for {} solution schedule is: {}".format(solution ,objfun_value),"#"*8)
        return objfun_value

    def SwapMove(self, solution, i ,j):
        '''Takes a list (solution)
        returns a new neighbor solution with i, j swapped
       '''
        solution = solution.copy()
        # job index in the solution:
        i_index = solution.index(i)
        j_index = solution.index(j)
        #Swap
        solution[i_index], solution[j_index] = solution[j_index], solution[i_index]
        return solution

    def TSearch(self):
        '''The implementation Tabu search algorithm with short-term memory and pair_swap as Tabu attribute.
        '''
        # Parameters:
        tenure =self.tabu_tenure
        tabu_structure = self.get_tabuestructure()  # Initialize the data structures
        best_solution = self.Initial_solution
        best_objvalue = self.Objfun(best_solution)
        current_solution = self.Initial_solution
        current_objvalue = self.Objfun(current_solution)

        print("#"*30, "Short-term memory TS with Tabu Tenure: {}\nInitial Solution: {}, Initial Objvalue: {}".format(
            tenure, current_solution, current_objvalue), "#"*30, sep='\n\n')
        iter = 1
        Terminate = 0
        while Terminate < 100:
            print('\n\n### iter {}###  Current_Objvalue: {}, Best_Objvalue: {}'.format(iter, current_objvalue,
                                                                                    best_objvalue))
            # Searching the whole neighborhood of the current solution:
            for move in tabu_structure:
                candidate_solution = self.SwapMove(current_solution, move[0], move[1])
                candidate_objvalue = self.Objfun(candidate_solution)
                tabu_structure[move]['MoveValue'] = candidate_objvalue

            # Admissible move
            while True:
                # select the move with the lowest ObjValue in the neighborhood (minimization)
                best_move = min(tabu_structure, key =lambda x: tabu_structure[x]['MoveValue'])
                MoveValue = tabu_structure[best_move]["MoveValue"]
                tabu_time = tabu_structure[best_move]['tabu_time']
                # Aspiration criteria and not tabu
                if tabu_time < iter or MoveValue < best_objvalue:
                    # make the move
                    current_solution = self.SwapMove(current_solution, best_move[0], best_move[1])
                    current_objvalue = self.Objfun(current_solution)
                    if current_objvalue < best_objvalue:
                        best_solution = current_solution
                        best_objvalue = current_objvalue
                        print("   best_move: {}, Objvalue: {} => Most imporving => Admissible".format(best_move,
                                                                                                      current_objvalue))
                    else:
                        print("   best_move: {}, Objvalue: {} => Least non-improving => Admissible".format(best_move,
                                                                                                      current_objvalue))
                        Terminate += 1
                    # update tabu_time for the move
                    tabu_structure[best_move]['tabu_time'] += tenure
                    iter += 1
                    break
                else:
                    tabu_structure[best_move]["MoveValue"] = float('inf')
                    print("   best_move: {}, Objvalue: {} => Tabu => Inadmissible".format(best_move, current_objvalue))
                    continue
        print('#'*50)
        print(best_solution,best_objvalue)

















test = TS(Path="Data_instances/Instance_30.xlsx",seed = 2019, tabu_tenure=3)
test.TSearch()