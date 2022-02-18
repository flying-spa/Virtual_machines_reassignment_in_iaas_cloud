import copy
from mini_main import x,y,goal_state,initial_state,dem_ram1,dem_cpu1
from time import time
import ss
n=y
g=0
moves=0
#cpu_dem = [5,1,1,1,1,1,1,1,1,1,4,1,3,1,1,1,1,1,1,1]
#ram_dem = [4096,1024,1024,1024,2048,2048,2048,2048,4096,1024,2048,1024,2048,4096,1024,2048,1024,4096,2048,2048]
cpu_dem=dem_cpu1
ram_dem=dem_ram1
#print("cpu_dem: ",cpu_dem)
cpu_cap = 32
#print("dem ram: ",ram_dem,"len of dem ram: ",len(ram_dem),"data type: ",type(ram_dem[0]))
ram_cap = 32678
goal_state_c=goal_state
initial_state_c=initial_state
explored= copy.deepcopy(initial_state)
num_of_instances=0
m=x
def final_state(s,m,n):
    for i in range(len(goal_state_c)):
        for j in range(n):
            if goal_state_c[i][j]!=s[i][j]:
                return False
    return True
def calc_cpu(s,i,n):
    summ=0
    for p in range(n):
        if s[i][p]==1:
            summ+=cpu_dem[p]
    return summ
def calc_ram(s,i,n):
    summ=0
    for p in range(n):
        if s[i][p]==1:
            summ+=ram_dem[p]
    return summ
def calc_h(s,m,n):
    h=0
    for i in range(m):
        for j in range(n):
            if goal_state_c[i][j]!=s[i][j]:
                h+=1
    return h/2
def calc_swap(s,i,j,k,m,n):
    res=copy.deepcopy(s)
    temp=res[k][j]
    res[k][j]=res[i][j]
    res[i][j]=temp
    return res


def calc_comp(explor,temp_state):
    for i in range(m):
        for j in range(n):
            if explored[i][j]!=temp_state[i][j]:
                return False
    return True
def calc_explored(temp_state,m,n):
    #print("In calc explored\n\tset of states(explored)is\n",explored,"\n\ttemp_state is\n",temp_state)
    for i in range(len(explored)):
        #print("In calc explored comparision\n\tset of states(explored[i])is\n",explored[i],"\n\ttemp_state is\n",temp_state)
        if calc_comp(explored[i],temp_state):
            return True
    return False
                    
        
def a_star(init_state,m,n):
    try:
        #goal_state_c=copy.deepcopy(goal_state)
        global moves
        if(final_state(init_state,m,n)):
            #print("Goal state Achieved\nflag_astar: ",ss.flag_astar)
            ss.flag_astar=1
            print("Goal state Achieved\nflag_astar: ")
            #return "Goal state Achieved"
        else:
            #print("It has enterd else case")
            global g
            g+=1
            fmin=99999
            flag=False
            state=[[0]*n]*m
            for i in range(m):
                #print("Cluster: ",i)
                cpu_i=calc_cpu(init_state,i,n)
                ram_i=calc_ram(init_state,i,n)
                #print("Cpu :", cpu_i,"\nram ",ram_i)
                for j in range(n):
                    if init_state[i][j]==0:
                        #print("in j loop\n\ti value is :",i," j value is ",j," fmin value is: ",fmin," g value is: ",g)
                        for k in range(m):
                            if k!=i:
                                #print("in k loop\n\ti value is :",i," j value is ",j," k value is ",k)
                                if init_state[k][j]==1:
                                    #print("Checking if it is feasible")
                                    if(((cpu_i+cpu_dem[j])<=cpu_cap) and ((ram_i+ram_dem[j])<=ram_cap)):
                                        #cpu_i+=cpu_dem[j]
                                        #ram_i+=ram_dem[j]
                                        #print("It is feasible")
                                        global num_of_instances
                                        num_of_instances+=1
                                        flag=True
                                        temp_state=calc_swap(init_state,i,j,k,m,n)
                                        #check if this state is explored temp_state)
                                        if(calc_explored(temp_state,m,n)==False):
                                            #print("Temp_state is:\n",temp_state)
                                            f=g+calc_h(temp_state,m,n)
                                            #print("f is ",f,"\t fmin is ",fmin,"\t g is ",g)
                                            if f<fmin:
                                                fmin=f
                                                #print("printing fmin ",fmin)
                                                state=copy.deepcopy(temp_state)
                                        
            if flag:
                #print("Level is",g,"\nGoing for the next iteration")
                #print("Obtained state is: \n",state)
                explored.append(state)
                #print("Explored states\n",explored)
                moves+=1
                a_star(state,m,n)
            else:
                print("Goal state not Achieved")
                ss.flag_astar=0
                #return "Goal state not Achieved"
    except:
        print("Goal state not Achieved bcz it is going for infinite loop")
        ss.flag_astar=0
trail=0
if __name__=="__main__":
    t0 = time()
    a_star(initial_state_c,m,n)
    t1 = time() - t0
    ss.time_astar=t1
    #print('time:', t1)
    #print('space:', num_of_instances)
    ss.space_astar=num_of_instances
    ss.moves_astar=moves


