""""""""""""""""""""""""""""""""""""""""""Documentation"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 

***Description***
The jain-himanshu folder contains 3 python files namely :
	random_search.py  |  conatins function "search" which searches path randomly in a world state full of obstacles to reach the goal.
	optimal_search.py |  conatins function "serarch" based on weighted A* search algorithm to find best shortest path to reach the
			     in a world state full of obstacles.
	suppClasss.py     |  nemonics for supportedClass. conatins two implemenatation : Priority Queue from the heapque class and
                             SquareGrid class that forms the squaregrid into graph.

***How to RUN***

for optimal path :
	python optimal_search.py
	<for input of world_state, robot_pose, goal_pose :  edit the file in commented portion>
	
	o/p :  list of Optimal path coordinates


for Random path :
	python random_search.py
	<for input of world_state, robot_pose, goal_pose, maximum number of path : edit the file in commented portion>


	o/p :  if path exist within maximum number of path 
			print "SUCCESS"
		   else path doesn't exist within maximum number of path
			print "NO path found in random search within maximum limit"
           ans show in both case
		   list of path coordinates

***Test correctness****

for world state = [[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,0,0,1,0],[0,0,0,0,1,0],[0,0,1,1,1,0],[0,0,1,0,1,0]]
    robot_pose, goal_pose = [(2,0),(5,5)]
	optimal search :  [(2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]

        random serach  : it depends on the number of AMximum path and also randomly result wither success (with path) or FAIL.					
	
	


*** Performance evaluation***
Optimal_search :  worst case performance : O(N)  N number of nodes/gridblocks
		  But gurrantees shortest path in short time.

random_search :  worst case performance : O(4*Maximumpath_number)
		But doesn't guarantee even the path
                However, probability fo finding a path increses as the number of maximum step increases. 


	








