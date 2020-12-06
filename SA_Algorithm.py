import pandas as pd
import random as rd

class SA():
    def __init__(self, Path, initial_temp, epoch, cooling_rate):
        self.Path = Path
        self.instance_dict = self.input_data()
        self.initial_temp = initial_temp
        self.epoch = epoch
        self.cooling_rate = cooling_rate


    def input_data(self):
        '''Takes the path of the excel file of the SMTWTP instances.
        Returns a dict of jobs number as Key and weight, processing time (hours) and due date (hours) as values.
        '''
        return pd.read_excel(self.Path, names=['Job', 'weight', "processing_time", "due_date"],
                                 index_col=0).to_dict('index')

    def get_InitialSolution(self, show=False):
        n_jobs = len(self.instance_dict) # Number of jobs
        # Producing a random schedule of jobs
        initial_solution = list(range(1, n_jobs+1))
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
    def SwapMove(self, li, show = False):
        '''Takes a list (solution)
        returns a new neighbor solution with randomly swapped elements
        '''
        pos1 = rd.randint(0, len(li) - 1)  # picking two random jobs
        pos2 = rd.randint(0, len(li) - 1)
        if pos1 != pos2:
            li[pos1], li[pos2] = li[pos2], li[pos1]
        else:
            self.SwapMove(li)
        if show == True:
            print("{} and {} are swapped, the current solution sequance is: {}".format(li[pos1], li[pos2], li))
        return li

    def SimuAnn(self):
        '''The implementation Simulated Annealing algorithm with a random swap move (neighborhood operator)
        Input : Initial temp(T_0), Epoch length(epo), Stopping Temp(T_f)
        Output: Best solution found and the Objfun Value of the corresponding solution
        '''
        initial_solution = self.get_InitialSolution()  # Randomly assign the initial solution
        # SA Parameters:
        T_0 = self.initial_temp
        epo = self.epoch
        cooling_fun = lambda x: x * self.cooling_rate
        T_f = 0.001




instances_10 = SA(Path="Data_instances/Instance_10.xlsx")
initial = instances_10.get_InitialSolution()
objvalue = instances_10.Objfun(initial,True)
