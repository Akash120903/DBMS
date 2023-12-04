at = [2, 5, 1, 0, 4]
bt = [6, 2, 8, 3, 4]
l = []
n = len(at)
for i in range(n):
    l.append([at[i], i])
l.sort()
ct = [0] * n
tat = [0] * n
wt = [0] * n
ctime = 0
i = 0
while i < n:
    if at[l[i][1]] <= ctime:
        ctime += bt[l[i][1]]
        ct[i] = ctime
        tat[i] = ct[i] - at[l[i][1]]
        wt[i] = tat[i] - bt[l[i][1]]
        i += 1
    else:
        ctime += 1
print("-" * 93)
print(
    "| Processes | Arrival time | Burst Time | Completion time | Turn-Around time | Waiting time |"
)
print("-" * 93)
for i in range(len(wt)):
    print(
        f"|{i+1:^11d}|{at[i]:^14d}|{bt[i]:^12d}|{ct[i]:^17d}|{tat[i]:^18d}|{wt[i]:^14d}|"
    )
print("-" * 93)

print("Completion time: ", ct)
print("Avg Turn around time: ", sum(tat) / n)
print("Avg Waiting time: ", sum(wt) / n)
