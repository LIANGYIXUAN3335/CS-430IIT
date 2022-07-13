 This program is used to assign most tasks with given number of resources.  This program is used  to solve traditional interval scheduling problem. 

for example: assign most lessons to classrooms , assign most jobs to machines......

​                

 ## Table of contents

- #### Usage

  You can create a txt file to store your data. 

  In this txt file ,the first line is the number of resource like classroom,machine and so on.

  Other lines representing the time interval that each task takes. [2 3] represent the begin time is 2 and end time is 3.

  After creating the txt file ,you need to put it in the same catalog with this program. Using pycharm / jupyter-notebook /python IDLE/cmd(must have installed python) to run this program . Then you will get a most job assignment.

- #### Algorithm construction

  ##### algorithm 1 :

  function: data_m_and_n() ---get data and sort jobs by end time 

  function: search_machine() ----using divide and conquer algorithm to find the best machine 

  function: job_for_each_machine() ---assign each job to a corresponding machine or drop it into     job_not_process list

  function: main() ---print the result

  ##### algorithm 2:

  function :data_m_and_n()--- get data and sort jobs by start time and end time

  function : max_m() ---calculate the number of machine to complete all jobs and assign each job to a corresponding machine or drop it to unjobs list.

  function : main() ----print the result

- #### Contribute

  Zhenya Zhang , Yixuan Liang , Yuhai Liu

 

 

 

 

 

 

 

 

 