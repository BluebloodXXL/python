import operator
arvTime_burstTime = {}
burstTime = []
burstTime_1 = []
arvTime = []
arvTime_1 = []
processNo = int(input("Enter number of process (Must enter the process which arrives at 0th second first)> "))

i = 0
while i < processNo:
    arvTime_1.append(int(input(f"Enter arrival time for process {i + 1} >")))
    burstTime_1.append(int(input(f"Enter execution time for process {i + 1} >")))
    if i > 0:
        arvTime_burstTime = {arvTime_1[i] : burstTime_1[i]}
    i = i + 1

arvTime_1 = arvTime_1.pop()
burstTime_1 = burstTime_1.pop()

# pop the dict -------- No need of that as the dict collects from index 1 of the array

# sort the dict
# sorted(sorted(arvTime_burstTime),key = operator.itemgetter(1))
sorted(arvTime_burstTime.items(),key = lambda x: x[1])
# print(arvTime_burstTime)

# Store keys and values
for keys,values in arvTime_burstTime:
    arvTime.append(keys)
    burstTime.append(values)

print(burstTime[2])


print("\n\nprocessID \t burstTime \t waitingTime \t turnAroundTime")

i = check = 0
waitingTime = turnAroundTime = totalWT = totalTAT = 0
while i < processNo-1:
    if check == 0:
        turnAroundTime = burstTime_1 + waitingTime
        print("\n  {:3d}\t\t\t{:3d}\t\t\t{:3d}\t\t\t\t{:3d}".format(i + 1, burstTime_1, waitingTime, turnAroundTime))
        totalWT = totalWT + waitingTime
        totalTAT = totalTAT + turnAroundTime
        waitingTime = waitingTime + burstTime_1
        check = 1
    turnAroundTime = burstTime[i] + waitingTime
    # print(f"\n\t{i + 1} \t\t\t {exeTime[i]} \t\t\t {waitingTime} \t\t\t\t {turnAroundTime}")
    print("\n  {:3d}\t\t\t{:3d}\t\t\t{:3d}\t\t\t\t{:3d}".format(i + 1, burstTime[i], waitingTime, turnAroundTime))
    totalWT = totalWT + waitingTime
    totalTAT = totalTAT + turnAroundTime
    waitingTime = waitingTime + burstTime[i]
    i = i + 1

print("\n\nAverage Waiting time is {:3.5f}".format(totalWT / processNo))
print("Average Turn around time is {:3.5f}".format(totalTAT / processNo))
