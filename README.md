# The-single-machine-total-weighted-tardiness-problem
The single machine total weighted tardiness problem (SMTWTP) is a
well-known NP-hard scheduling problem. There are n jobs to be scheduled
on a single machine that can handle only one job at a time. Each of n
jobs (numbered 1, . . . , n) is to be processed without interruption.
Job *i* ∈ *n* becomes available for processing at time zero, requires an
integer processing time *p*<sub>*i*</sub>, and has a positive weight
*w*<sub>*i*</sub> and a due date *d*<sub>*i*</sub>.  
For a given processing order of the jobs, the (earliest) completion time
*C*<sub>*i*</sub> and the tardiness
*T*<sub>*i*</sub> = *m**a**x*{*C*<sub>*i*</sub> − *d*<sub>*i*</sub>, 0}
of job *i* ∈ (*i* = 1, ..., *n*) can be computed. The objective is to
find a processing order of the jobs that minimizes the total weighted
tardiness:
*m**i**n*∑<sub>*i*</sub>*w*<sub>*i*</sub> × *T*<sub>*i*</sub>.

Data for three example problem instances are provided [here](https://github.com/taylankabbani/The-single-machine-total-weighted-tardiness-problem/tree/master/Data_instances)

## [FirstDescent Algorithm](https://github.com/taylankabbani/The-single-machine-total-weighted-tardiness-problem/blob/master/FirstDescent_algorithm.py)

The developed local search algorithm to solve SMTWTP is described as
follows. The solution presentation is the permutation of n numbers of
the jobs to be done in the set {1, 2,..., n}, where the
*i*<sup>*th*</sup> number in the permutation denotes that the job is
the *i*<sup>*th*</sup> job to be processed. For example, a sequence of
5-job schedules, 5-3-1-2-4 is simply represented as {5,3,1,2,4}. The
initial solution is generated by producing a random schedule of jobs,
and the set of neighboring solutions N(X) is sampled by swap at random
*i*<sup>*th*</sup> and *j*<sup>*th*</sup> number of the current
solution. The first improvement (first descent) strategy move is
applied. The stopping criteria is set to 100 iteration without finding
an improving solution.
| n_jobs |                                                  Initial Solution                                                 | Objfun Value |                                                  Final Solution                                                  | Objfun Value |
|:------:|:-----------------------------------------------------------------------------------------------------------------:|:------------:|:----------------------------------------------------------------------------------------------------------------:|:------------:|
| 10     | [4, 7, 9, 1, 5, 3, 10, 6, 8, 2]                                                                                   | 39           | [2, 3, 1, 4, 8, 10, 5, 9, 7, 6]                                                                                  | 13.24       |
| 20     | [17, 14, 19, 18, 13, 20, 3, 2, 8, 6,  5, 15, 9, 1, 10, 11, 7, 12, 16, 4]                                          | 70.75        | [18, 11, 3, 2, 1, 14, 5, 9, 4, 10, 20, 8, 13, 15, 19, 7, 6, 12, 17, 16]                                         | 19.31      |
| 30     | [13, 2, 25, 24, 21, 22, 23, 6, 28, 27,  3, 5, 8, 18, 15, 14, 9, 30, 29, 26, 10,  20, 17, 1, 19, 11, 7, 12, 16, 4] | 479.4        | [28, 11, 26, 8, 16, 20, 29, 7, 30, 27, 2, 21, 18, 24, 14, 22, 5, 10, 9, 1, 19, 6, 13, 4, 17, 15, 12, 25, 23, 3] | 153.79        |


## [Simulated Annealing (SA) Algorithm](https://github.com/taylankabbani/The-single-machine-total-weighted-tardiness-problem/blob/master/Simulated_Annealing%20algorithm/SA_Algorithm.py)
The swap move is used to develop a Simulated Annealing (SA) algorithm with the following
temperature = 1000, geometric cooling schedule with a cooling rate of 0.99, epoch len
criteria as the temperature achieves a very small value (e.g., 0.001).
SA algorithm is a stochastic algorithm; therefore, in order to evaluate its performance, the
along with the best and worse performance is being reported for each problem instance.
|  | Temperature = 1000 |  |  | Temperature = 100000 |  |  |
|-|:-:|-|-|:-:|-|-|
| n_jobs | Worst <br>Solution | Best <br>Solution | Average <br>Performance | Worst <br>Solution | Best <br>Solution | Average <br>Performance |
| 10 | 13.24 | 13.24 | 13.24 | 13.24 | 13.24 | 13.24 |
| 20 | 19.19 | 18.99 | 19.1 | 19.28 | 19.01 | 19.19 |
| 30 | 150.9 | 150.3 | 150.54 | 150.9 | 150.5 | 150.7 |

![](https://github.com/taylankabbani/The-single-machine-total-weighted-tardiness-problem/blob/master/Simulated_Annealing%20algorithm/Out.xlsx/img_1000.png)

## [Tabu Search (TS) Algorithm](https://github.com/taylankabbani/The-single-machine-total-weighted-tardiness-problem/blob/master/TS_longMemmory.py)
**Long-term memory TS** is being designed with diversification
technique, where the frequency of moves is recorded to be used as
penalty when calculating the move value (Value = Penalized\_weight \*
frequency). The Swap move between two jobs is being considered as the
tabu attribute. An aspiration criterion set to when the objective
function value is better than the best known one. The termination
condition is set to 100 consecutive iterations with no best (the
incumbent) solution found.
The algorithm is being tested with two different tabu tenure, 3 and 6,
with Penalization weight set to 0.6, 0.8 respectively. (Table Above)
|  | Tabu Tenure = 3, <br>Penalization weight = 0.6 |  | Tabu Tenure = 6<br>Penalization weight = 0.8 |  |
|-|:-:|-|:-:|-|
| n_jobs | Final Solution | ObjValue | Final Solution | ObjValue |
| 10 | [3, 2, 1, 4, 8, 10, 5, 9, 7, 6] | 13.24 | [3, 2, 1, 4, 8, 10, 5, 9, 7, 6] | 13.24 |
| 20 | [11, 3, 2, 1, 14, 18, 5, 9, 4,<br> 10, 20, 8, 13, 19, 7, 12, 17<br>, 15, 6, 16] | 19.09 | [3, 11, 2, 14, 1, 5, 9, 18, 4, <br>10, 20, 8, 13, 19, 7, 12, 17,<br> 6, 15, 16] | 19 |
| 30 | [29, 28, 8, 30, 16, 20, 7, 11, <br>26, 27, 18, 2, 24, 14, 5, 9,<br> 10, 21, 19, 1, 6, 13, 22, 4,<br> 17, 15, 12, 25, 23, 3] | 150.3 | [20, 8, 16, 30, 7, 29, 28, 11,<br> 26, 27, 18, 2, 21, 24, 14, 5,<br> 9, 10, 19, 1, 6, 13, 4, 22, 17,<br> 12, 15, 25, 23, 3] | 150.5 |
