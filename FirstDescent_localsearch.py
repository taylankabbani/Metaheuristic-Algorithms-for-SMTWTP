import pandas as pd
import random as rd


def input_data(file_path):
    '''Takes the path of the excel file of the SMTWTP instances.
    Returns a dict of jobs number as Key and weight, processing time (hours) and due date (hours) as values.
    '''
    return pd.read_excel(file_path,names = ['Job','weight',"processing_time", "due_date"],index_col=0).to_dict('index')

instance_10 = input_data("Data_instances/Instance_10.xlsx")



def Initial_solution(dict, show=False):
    '''Produce a random schedule of jobs
    '''
    n_jobs = len(dict) # Number of jobs
    # Producing a random schedule of jobs 
    initial_solution = list(range(1, n_jobs+1))
    rd.seed(2012)
    rd.shuffle(initial_solution)
    if show == True:
        print("initial Random Solution: {}".format(initial_solution))
    return initial_solution




def Objfun(solution, dict, show = False):
    '''Takes a set of scheduled jobs, dict (input data)
    Return the objective function value of the solution
    '''
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
            print("\n{}th job tardiness: {}".format(job, T_i))
    print("\n","#"*8, "The Objective function value for {} solution schedule is: {}".format(solution ,objfun_value),"#"*8)

initial = Initial_solution(instance_10)
# Objfun(initial, instance_10, show_taridness=True)


def SwapMove(li, pos1, pos2):
    '''Takes a list (solution), position1 and position2
    return a new neighbor solution with swapped elements
    '''
    li[pos1], li[pos2] = li[pos2], li[pos1]
    print(li)
    

def First_descent(initial_solution, dict):
    '''Then implementation of a swap move (neighborhood operator) to improve the initial solution
    first improvement (first descent) strategy in applying the move.
    '''

