exeTime = []
processNo = int(input("Enter number of process > "))

i = 0
while i < processNo:
    exeTime.append(int(input(f"Enter execution time for process {i + 1} >")))
    i = i + 1

print("\n\nprocessID \t burstTime \t waitingTime \t turnAroundTime")

i = waitingTime = turnAroundTime = totalWT = totalTAT = 0
while i < processNo:
    turnAroundTime = exeTime[i] + waitingTime
    # print(f"\n\t{i + 1} \t\t\t {exeTime[i]} \t\t\t {waitingTime} \t\t\t\t {turnAroundTime}")
    print("\n  {:3d}\t\t\t{:3d}\t\t\t{:3d}\t\t\t\t{:3d}".format(i + 1, exeTime[i], waitingTime, turnAroundTime))
    totalWT = totalWT + waitingTime
    totalTAT = totalTAT + turnAroundTime
    waitingTime = waitingTime + exeTime[i]
    i = i + 1

print("\n\nAverage Waiting time is {:3.5f}".format(totalWT / processNo))
print("Average Turn around time is {:3.5f}".format(totalTAT / processNo))
