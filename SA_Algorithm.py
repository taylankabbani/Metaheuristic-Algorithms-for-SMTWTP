import pandas as pd
import random as rd
import math

class SA():
    def __init__(self, Path, initial_temp, epoch, cooling_rate):
        self.Path = Path
        self.instance_dict = self.input_data()
        self.initial_temp = initial_temp
        self.epoch = epoch
        self.cooling_rate = cooling_rate
        self.Best_solution, self.Best_objvalue = self.SimuAnn()


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
        li = li.copy()
        pos1 = rd.randint(0, len(li) - 1)  # picking two random jobs
        pos2 = rd.randint(0, len(li) - 1)
        if pos1 != pos2:
            li[pos1], li[pos2] = li[pos2], li[pos1]

        while pos1 == pos2:
            pos1 = rd.randint(0, len(li) - 1)  # picking two random jobs
            pos2 = rd.randint(0, len(li) - 1)  
            if pos1 != pos2:
                li[pos1], li[pos2] = li[pos2], li[pos1]
                break
        if show == True:
            print("{} and {} are swapped, the current solution sequance is: {}".format(li[pos1], li[pos2], li))
        return li

    def SimuAnn(self):
        '''The implementation Simulated Annealing algorithm with a random swap move (neighborhood operator)
        Input : Initial temp(T_0), Epoch length(epo), Stopping Temp(T_f)
        Output: Best solution found and the Objfun Value of the corresponding solution
        '''
    
        # SA Parameters:
        T_0 = self.initial_temp
        maxepo = self.epoch
        cooling_fun = lambda x: x * self.cooling_rate
        T_f = 0.001

        best_solution = []
        best_objvalue = float('inf')
        current_solution = self.get_InitialSolution()  # Randomly assign the initial solution at the first iteration.
        current_objvalue = self.Objfun(current_solution)

        T = T_0  # Current temp
        current_iter = 1
        print("\n\nNumber of jobs to be scheduled: {}".format(len(current_solution)))
        print("\nInitial Solution: {}    Initial Objfun value: {}\n\n".format(current_solution, current_objvalue))

        while T >= T_f :
            epoch = int(0)
            while epoch < maxepo:

                print("### iter: {}/ epoch: {} ### current_temp: {}, current_objfun: {}, best_Objfun: {}".format(current_iter, epoch, T,current_objvalue,best_objvalue))

                #generate neighbor by randomly swap move
                candidate_solution = self.SwapMove(current_solution) 
                candidate_objvalue = self.Objfun(candidate_solution)

                # Improving solution found
                if candidate_objvalue <= current_objvalue:  
                    current_solution, current_objvalue = candidate_solution ,candidate_objvalue
                   # Update best solution 
                    if current_objvalue < best_objvalue:
                        best_solution, best_objvalue = current_solution, current_objvalue

                    print(" "*5, "Candidate Solution: Objfun= {},  Sequence= {}   =>  Improved Solution  => Accepted\n".format(candidate_objvalue, candidate_solution))   
                
                #non_imporving solution
                else:
                    degradation = candidate_objvalue - current_objvalue
                    metropolis = math.exp(-(degradation/T))
                    x = rd.random()
                    # Accepting non-improvment solution based on metropolis criterion
                    if x <= metropolis:
                        current_solution, current_objvalue = candidate_solution ,candidate_objvalue
                        print(" "*5, "Candidate Solution: Objfun= {},  Sequence= {}   =>  Non_improved Solution => Metropolis => Accepted\n".format(candidate_objvalue, candidate_solution))   
                    else:
                        print(" "*5, "Candidate Solution: Objfun= {},  Sequence= {}   =>  Non_improved Solution => Metropolis  => Not Accepted\n".format(candidate_objvalue, candidate_solution)) 
                #Update param
                epoch += 1
            # Update Temp & iter
            T = cooling_fun(T)
            current_iter += 1
        print('#'*30, '\nNumber of iteration performed: {}\nFinal Temperature: {}\nBest Objvalue: {}\nBest Solution: {}'.format(current_iter, T, best_objvalue, best_solution))
        return best_solution, best_objvalue
                    


# Example:
## 5 runs for each instance:
# results = []
# for i in range(5):
#     instances_10 = SA(Path="Data_instances/Instance_10.xlsx", initial_temp = 1000, epoch = 3, cooling_rate = 0.99)
#     results.append(instances_10.Best_objvalue)

