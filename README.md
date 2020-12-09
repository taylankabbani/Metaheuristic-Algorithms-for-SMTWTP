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
Data for three example problem instances are provided here
