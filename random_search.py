import numpy as np
import queue
import random
from suppClass import Grid
import math
 
def Search(world,start,goal):
    mat = np.matrix(world)
    row,col = mat.shape
    graph = Grid(row,col)
    graph.walls =list(zip(np.where(mat==1)[0].tolist(),np.where(mat==1)[1].tolist()))
    del(mat)
    
	came_from= []
    came_from.append(start)
    step =0 
    stepsQ = queue.Queue(maxsize=math.floor(math.sqrt(Maximum_steps)))
    current = start
    stepsQ.put(start)
	
    while step!= Maximum_steps :
        if current == goal:
           break
		   
		nbhrs =  list(graph.neighbors(current))
        while len(nbhrs) != 0:        
            ch = random.choice(nbhrs)
            if ch in list(stepsQ.queue) and len(nbhrs)>1 :
                del(nbhrs[nbhrs.index(ch)])
            else : 
                if stepsQ.full():
                    stepsQ.get()
                stepsQ.put(ch)
                break
				
        came_from.append(ch)
        current = ch    
        step=step+1
		
    path = came_from
    if goal == came_from[-1]:
        print "SUCCESS"
    else :
        print "NO path found in random search within the maximum limit"
    return path    
        
if __name__ == '__main__' :	
	Maximum_steps            = 50
	world_state              = [[0,0,1,0,0,0],[0,0,1,0,0,0],[0,0,0,0,1,0],[0,0,0,0,1,0],[0,0,1,1,1,0],[0,0,1,0,1,0]]
	robot_pose,goal_pose     = [(2,0),(5,5)]
	path                     = Search(world_state,robot_pose,goal_pose)
	print path
