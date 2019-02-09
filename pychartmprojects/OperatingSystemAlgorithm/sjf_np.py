burstTime = []
arvTime = []
processNo = int(input("Enter number of process > "))

i = 0
while i < processNo:
    arvTime.append(int(input(f"Enter arrival time for process {i + 1} >")))
    burstTime.append(int(input(f"Enter execution time for process {i + 1} >")))
    i = i + 1

burstTime_1 = burstTime[0]
arvTime_1 = arvTime[0]
burstTime.pop(0)
arvTime
burstTime.sort()

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
