import heapq

at = [2, 5, 1, 0, 4]
bt = [6, 2, 8, 3, 4]
priority = [-2, -3, -4, -5, -5]
n = len(at)
l = []
for i in range(n):
    l.append([at[i], i])
l.sort()
ctime = 0
ct = [0] * n
tat = [0] * n
wt = [0] * n
queue = []
completed = 0
while completed < n:
    for i in range(len(l)):
        if l[i] and at[l[i][1]] <= ctime:
            heapq.heappush(queue, [priority[l[i][1]], l[i][1]])
            l[i] = None
    if not queue:
        ctime += 1
        continue
    pt, pid = heapq.heappop(queue)
    ctime += bt[pid]
    completed += 1
    ct[pid] = ctime
    tat[pid] = ct[pid] - at[pid]
    wt[pid] = tat[pid] - bt[pid]
print("-" * 104)
print(
    "| Processes | Arrival time | Burst Time | Priority | Completion time | Turn-Around time | Waiting time |"
)
print("-" * 104)
for i in range(len(wt)):
    print(
        f"|{i + 1:^11d}|{at[i]:^14d}|{bt[i]:^12d}|{priority[i]:^10d}|{ct[i]:^17d}|{tat[i]:^18d}|{wt[i]:^14d}|"
    )
print("-" * 104)


print("completion time: ", ct)
print("Avg Turn around time: ", sum(tat) / n)
print("Avg Waiting time: ", sum(wt) / n)
