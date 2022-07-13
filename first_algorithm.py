import heapq
def data_m_and_n(): #get data from txt.
    with open("./test.txt", "r") as f:
        data=[]
        for line in f.readlines():
            line = line.strip('\n')
            data.append(list(map(int,line.split())))
    m=data[0]
    data.remove(m)
    m = m[0]
    n=len(data)
    jobssort=[]
    for i in range(n):
        jobssort.append(data[i])
    jobssort.sort(key = lambda x: x[1])
    #Sort tasks by end time
    return jobssort,data,m,n

def search_machine(starttime,priority_machine,n):
    #get the machine to assign the current job
    #which last job's end time is the nearliest to the start time of current job
    left, right = 0, n-1  # Initialize the left and right endpoint positions
    while left < right:  # When the condition is legal
        if priority_machine[right][0]<=starttime :
            left = right
        elif  left >= right-1:
            break
        else:
            mid = left + (right - left) // 2  # Get the midpoint, or the left if it's even
            if priority_machine[mid][0] > starttime  :  # If the current number of positions is greater than the inserted value
                right = mid   # Update the right endpoint
            elif priority_machine[mid][0] < starttime:  # If the current number of positions is less than the inserted value
                left = mid   # 更新左端点
            elif priority_machine[mid][0] == starttime:  # If the current number of positions is less than the inserted value
                left = mid
    return (priority_machine[left])

def Job_for_each_machine(): # assign and Calculate the jobs each machine does
    Machine = [] # store jobs for each machine
    data = data_m_and_n()
    jobs = data[0]
    len_machine =data[2]
    len_job = data[3]
    priorityQueue_machine = [(0,i) for i in range(len_machine)]  #Storage machine of priority queue by termination time
    # For example, [(2, 0), (4, 1)] means that machine 0 terminates at 2
    # Machine number 1 terminates at 4 so (2,0) comes before (4, 1)
    jobs_not_process = []
    for i in range(len_machine):
        Machine.append([])
        # priorityQueue_machine.append((0,i))# 0 represent the least time that a job can begin
    for j in range(len_job):
        current_job =jobs[j]
        print(current_job)
        if current_job[0]<priorityQueue_machine[0][0]: #In case of a conflict, drop the current task and store it in job_not_process
            jobs_not_process.append(current_job)
        else:                                         #If no conflict occurs, save the task to the machine with the highest priority

            machine = search_machine(current_job[0],priorityQueue_machine,len_machine)

            Machine[machine[1]].append(current_job)
            priorityQueue_machine.remove(machine)
            heapq.heappush(priorityQueue_machine,(current_job[1],machine[1]))
        print(Machine)
        print(priorityQueue_machine)
    return Machine,jobs_not_process,len_job,len_machine
if __name__=="__main__": # use all the functions and print result
    data = Job_for_each_machine()
    unjobs = data[1]
    jobs = data[0]
    len_jobs = data[2]
    len_machine = data[3]
    if len(unjobs) == 0:
        for i in range(len_machine):
            print("Machine #{} has jobs:".format(i+1))
            print(jobs[i])
    if len(unjobs) != 0:
        a = 0
        for i in range(len_machine):
#             s = len(max_jobs[i])
            print("Machine #{} has jobs:".format(i+1))
            print(jobs[i])
    print("Jobs not processed:\n {}".format(unjobs))
    print("{} number of jobs out of {} total jobs".format(len_jobs-len(unjobs),len_jobs))
