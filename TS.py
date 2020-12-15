import pandas as pd
import random as rd
from itertools import combinations
import math

class TS():
    def __init__(self, Path, seed):
        self.Path = Path
        self.seed = seed
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
        Returns a dict of tabu attributes(pair of jobs that are swapped) as keys and [tabu_time, SwapValue (for
        candidate solutions)]
        '''
        dict = {}
        for swap in combinations(self.instance_dict.keys(), 2):
            dict[swap] = {'tabu_time': 0, 'SwapValue': 0}
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
        '''The implementation Tabu search algorithm with short-term memory and pair swap as Tabu attribute.
        Input :
        Output: Best solution found and the Objfun Value of the corresponding solution
        '''
        tabu_structure = self.get_tabuestructure()  # Initialize the data structures
        current_solution = self.Initial_solution
        current_objvalue = self.Objfun(current_solution)
        # print("Initial Solution: {}, objvalue: {}".format(self.Initial_solution, self))

        # Searching the whole neighborhood of the current solution:
        for neighbor in











test = TS(Path="Data_instances/Instance_10.xlsx",seed = 2012)