import copy
from time import time
from mini_main import x,y,goal_state,initial_state, dem_ram1, dem_cpu1
import ss
goal_state_c=goal_state
initial_state_c=initial_state
#m is the Number of Clusters
m = x
#n is the Number of Customers
n = y
#cpu is the CPU Demand requested by the Customers
cpu=dem_cpu1
#ram is the RAM Demand requested by the Customers
ram=dem_ram1
#cpu_max is the Maximum cpu of Server
cpu_max = 32
#ram_max is the Maximum RAM Capacity of Server
ram_max = 32768
#no_of_moves to find the total moves done to achieve goal state
no_of_moves=0
#hc_mat is the array where that particular customer is heavy or not
hc_mat = []
for i in cpu:
    if i>1:
        hc_mat.append(1)
    else:
        hc_mat.append(0)
#hc is the total No.of Heavy Customers
hc=sum(hc_mat)
itr_max=20
#final_state function is used to check whether initial and goal state are same or not
def final_state(s):
    for i in range(m):
        for j in range(n):
            if(goal_state_c[i][j]!=s[i][j]):
                return False
    return True
#calc_cpu function is used to find the cpu requested by the customer in that particular cluster
def calc_cpu(s, x):
    summ = 0;
    for i in range(n):
        if(s[x][i]==1):
            summ+=cpu[i]
    return summ
#calc_ram function is used to find the ram requested by the customer in that particular cluster
def calc_ram(s, x):
    summ = 0;
    for i in range(n):
        if(s[x][i]==1):
            summ+=ram[i]
    return summ
#calc_hc function is used to find the total number of heavy customers in that particular cluster
def calc_hc(s, x):
    summ = 0;
    for i in range(n):
        if(s[x][i]==1):
            summ+=hc_mat[i]
    return summ
#find_cluster function is used the cluster where the goal state has value 1 for that particular customer
def find_cluster(i):
    x=-1
    for j in range(m):
        if(goal_state_c[j][i]==1):
            x = j
    return x
#idmh function is used to reach goal state from initial state using IDMH Algorithm
def idmh(state, m,  n):
    #traverse along the column
    global no_of_moves
    no_of_moves=0
    itr=0
    while itr<itr_max:
        #print("itr iteration number: ",itr)
        for i in range(n):
            for j in range(m):
                if(state[j][i]==1):
                    #j th cluster
                    #check the customer with the goal state
                    if(state[j][i]!=goal_state_c[j][i]):
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
        if(final_state(state)==True):
            return True
        itr+=1
    return False
    

t0=time()    
if(idmh(initial_state_c,m,n)):
    ss.flag_idmh=1
    print("Goal State achieved\nNo.of moves: ",no_of_moves)
else:
    ss.flag_idmh=0
    print("Goal state not achieved\n")
t1=time()-t0
ss.time_idmh=t1
#print('time:', t1)
ss.moves_idmh=no_of_moves
