import SA_Algorithm

def Performance(Path, temp):
    results = []
    for i in range(5):
        instance = SA_Algorithm.SA(Path, initial_temp = temp, epoch = 3, cooling_rate = 0.99)
        results.append(instance.Best_objvalue)
    print("Worst Soluton: {}\nBest Solution: {}\nAvg_performance: {}".format(max(results),min(results), sum(results)/len(results)))
    return results

# Testing for Temp = 1000
# job_10 = Performance("Data_instances/Instance_10.xlsx", 1000)
# job_20 = Performance("Data_instances/Instance_20.xlsx", 1000)
# job_30 = Performance("Data_instances/Instance_30.xlsx", 1000)

# Testing for Temp = 100000
# job_10 = Performance("Data_instances/Instance_10.xlsx", 100000)
# job_20 = Performance("Data_instances/Instance_20.xlsx", 100000)
# job_30 = Performance("Data_instances/Instance_30.xlsx", 100000)


SA_Algorithm.SA(Path = "Data_instances/Instance_30.xlsx", initial_temp = 1000, epoch = 3, cooling_rate = 0.99).Save_file("out_1000.xlsx")
SA_Algorithm.SA(Path = "Data_instances/Instance_30.xlsx", initial_temp = 100000, epoch = 3, cooling_rate = 0.99).Save_file("out_100000.xlsx")