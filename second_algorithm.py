def data_m_and_n():
    with open("./1.txt", "r") as f:
        data=[]
        for line in f.readlines():
            line = line.strip('\n')
            data.append(list(map(int,line.split())))
    m=data[0]
    data.remove(m)
    # Format the initial data with the data variable, save the number of machines separately and reformat the data
    n=len(data)
    data.sort(key=lambda x:(x[0],x[1]))
    # Tasks are first sorted in ascending order according to the start time and then in descending order according to the end time.
    # By using sort function, the time complexity is nlogn
    timesort=[]
    for i in range(n):
        timesort.append([i,data[i][0],1])
        timesort.append([i,data[i][1],-1])
    timesort.sort(key = lambda x:x[1])
    # prioritize the task completed first to match the next starting task,
    # and then perform a linear ordering for all time points with time complexity O(n).
    # The coding structure is as follows: the first digit corresponds to the current task number,
    # the second digit corresponds to the position of the current time interval, the third digit 1 indicates the start, and -1 indicates the end
    return timesort,data,m
def max_m():
    timesort = data_m_and_n()[0]
    n = len(timesort)
    list_link = [[] for _ in range(n // 2 )]
    total = [[0, 0] for _ in range(n + 1)]
    queue = []
    num = [0 for _ in range(n // 2 )]
    for i in range(n):
        total[i + 1][0] = total[i][0] + timesort[i][2]
        total[i + 1][1] = timesort[i][0]
        # The minimum number of machines is recorded. When a start time passes, the list total increases by 1.
        # When an end time is met, the current value of the list decreases by 1
    for i in range(1, len(total)):
        if total[i - 1][0] < total[i][0] and len(queue) < 1:
            list_link[total[i][1]].append(total[i][1])
            num[total[i][1]] = len(list_link[total[i][1]])
        elif total[i - 1][0] > total[i][0]:
             queue.append(total[i][1])
             # Use queues to store completed work. When it comes to the next start work,
             # the first completed work matches the first started work.
             # Because the sample has increased a lot in the number of end tasks at the same time,
             # the current task at the beginning, there is the task of the maximum time interval,
             # though its start time is after the stage of the front, but covered more tasks,
             # also cannot be regarded as the first end, because the other task priority matching,
             # judgment, by tracing if can increase the time complexity,
             # Therefore, the maximum value of task connection is used to judge the connection of the current task.
        elif total[i - 1][0] < total[i][0] and len(queue) > 0:
            e =[]
            s={}
            for j in queue:
                e.append(num[j])
                s[num[j]]=j
            a = s[max(e)]
            queue.remove(a)
            # Here using a list once and it's O(nm) over time.
            list_link[a].append(total[i][1])
            list_link[total[i][1]],list_link[a]=list_link[a],list_link[total[i][1]]
            num[total[i][1]] = len(list_link[total[i][1]])
            num[a] = 0
            # Here, a matrix is selected to record the flow of each work. If the current flow has subsequent flow,
            #  the current flow is merged into the latest flow, and the previous flow is denoted as 0
    while list_link[-1]==[]:
        list_link.remove(list_link[-1])
    list_link.sort(key = lambda x:len(x),reverse=True)
    # Finally, remove the rows equal to [] in the matrix, sort them according to the number of elements in the row,
    # and the obtained elements are the corresponding number of the task
    return list_link
if __name__=="__main__":
    min_m=max_m()
    data=data_m_and_n()[1]
    m=data_m_and_n()[2][0]
    total_jobs=len(data)
    a=0
    for i in range(m):
        print("Machine #{} has jobs:".format(i+1))
        a=a+len(min_m[i])
        for j in min_m[i]:
            print(data[j])
    unjobs=min_m[m::]
    if len(unjobs)!=0:
        print('Jobs not processed:')
        for i in range(len(unjobs)):
            for j in unjobs[i]:
                print(data[j])
        print("{} number of jobs out of {} total jobs".format(a,total_jobs))