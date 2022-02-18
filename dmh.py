import copy
from time import time
from mini_main import x,y,goal_state,initial_state, dem_ram1, dem_cpu1
import ss
goal_state_c=copy.deepcopy(goal_state)
initial_stat,e_c=copy.deepcopy(initial_state)
m = x
#n=20
n = y
hc = 8
cpu=dem_cpu1
ram=dem_ram1
#cpu = [3,3,4,3,4,1,1,1,1,3,5,3,2,2,4,3,3,4,2,4];
#ram = [4096,1024,1024,1024,2048,2048,2048,2048,4096,1024,2048,1024,2048,4096,1024,2048,1024,4096,2048,2048];
cpu_max = 32;
no_of_moves=0
ram_max = 32768;
hc_mat = []
for i in cpu:
    if i>1:
        hc_mat.append(1)
    else:
        hc_mat.append(0)
def final_state(s):
    for i in range(m):
        for j in range(n):
            if(goal_state_c[i][j]!=s[i][j]):
                return False
    return True
def calc_cpu(s ,  x):
    summ = 0;
    for i in range(n):
        if(s[x][i]==1):
            summ+=cpu[i]
    return summ
def calc_ram(s,  x):
    summ = 0;
    for i in range(n):
        if(s[x][i]==1):
            summ+=ram[i]
    return summ
def calc_hc(s,  x):
    summ = 0;
    for i in range(n):
        if(s[x][i]==1):
            summ+=hc_mat[i]
    return summ
def find_cluster( i):
    x=-1
    for j in range(m):
        if(goal_state_c[j][i]==1):
            x = j
    return x
def dmh(state, m,  n):
    #traverse along the column
    global no_of_moves
    no_of_moves=0
    for i in range(n):
        for j in range(m):
            if(state[j][i]==1):
                #j th cluster
                #check the customer with the goal state
                if(state[j][i]!=goal_state[j][i]):
                    #cout<<"customer no: "<<i<<endl;
                    x = find_cluster(i);
                    #cout<<"x value: "<<x<<endl;
                    curr_cpu = calc_cpu(state,x);
                    #cout<<"current cpu: "<<curr_cpu<<endl;
                    curr_ram = calc_ram(state,x);
                    #cout<<"current ram: "<<curr_ram<<endl;
                    curr_hc = calc_hc(state,x);
                    #cout<<"current hc: "<<curr_hc<<endl;

                    #check for constraints
                    if(curr_cpu+cpu[i]<=cpu_max and curr_ram+ram[i]<=ram_max and curr_hc+hc_mat[i]<=hc):
                        #swap
                        #cout<<"contraint satisfied\n";
                        no_of_moves+=1
                        tmp = state[j][i]
                        state[j][i] = state[x][i]
                        state[x][i] = tmp
                        #print("after swapping: \n",state)
                break
    return final_state(state)

t0=time()    
if(dmh(initial_state_c,m,n)):
    ss.flag_dmh=1
    print("Goal State achieved\nmoves: ",no_of_moves)
else:
    ss.flag_dmh=0
    print("Goal state not achieved\nmoves: ",no_of_moves)
t1=time()-t0
ss.time_dmh=t1
#print('time:', t1)
ss.moves_dmh=no_of_moves
