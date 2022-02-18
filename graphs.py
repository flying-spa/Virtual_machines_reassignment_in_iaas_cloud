import xlrd
import matplotlib.pyplot as plt
import numpy as np

book_1=xlrd.open_workbook('C:/Users/sutha/AppData/Local/Programs/Python/Python37-32/Mini Project/trial.xlsx')
sheet_4=book_1.sheet_by_name('Sheet 1')
rows_1 = []
for i in range(sheet_4.nrows):
    columns_1 = []
    for j in range(sheet_4.ncols):
        x_2=sheet_4.cell(i, j).value
        #print(x)
        if x_2!='':
            columns_1.append(x_2)
    if len(columns_1)!=0:
        rows_1.append(columns_1)
#print (rows_1)
#common variables
no_of_nodes=[20,30,40,50]
no_of_success_m1=["m1+0","m1+1","m1+2","m1+3"]
no_of_success_n_cont=["n/5","n/4","n/3","n/2"]
no_of_success_n_cont_1=[5,4,3,2]
no_of_success_hc=[20,30,50]

#astar variables    
astar_no_of_success=[0,0,0,0]
astar_no_of_success_u=[]

astar_no_of_success_m=[0,0,0,0]
astar_no_of_generated_nodes=[0,0,0,0]

astar_no_of_success_n_cont_2=[0,0,0,0]
astar_no_of_success_hc_1=[0,0,0]

astar_no_of_moves=[0,0,0,0]
astar_no_of_moves_m=[0,0,0,0]
astar_no_of_moves_mc=[0,0,0,0]
astar_no_of_moves_hc=[0,0,0]

#dmh variables    
dmh_no_of_success=[0,0,0,0]
dmh_no_of_success_u=[]

dmh_no_of_success_m=[0,0,0,0]
dmh_no_of_generated_nodes=[0,0,0,0]

dmh_no_of_success_n_cont_2=[0,0,0,0]

dmh_no_of_success_hc_1=[0,0,0]

dmh_no_of_moves=[0,0,0,0]
dmh_no_of_moves_m=[0,0,0,0]
dmh_no_of_moves_mc=[0,0,0,0]
dmh_no_of_moves_hc=[0,0,0]

#idmh variables    
idmh_no_of_success=[0,0,0,0]
idmh_no_of_success_u=[]

idmh_no_of_success_m=[0,0,0,0]
idmh_no_of_generated_nodes=[0,0,0,0]

idmh_no_of_success_n_cont_2=[0,0,0,0]

idmh_no_of_success_hc_1=[0,0,0]

idmh_no_of_moves=[0,0,0,0]
idmh_no_of_moves_m=[0,0,0,0]
idmh_no_of_moves_mc=[0,0,0,0]
idmh_no_of_moves_hc=[0,0,0]

#to find number of success for n=20,30,40,50
for i in range(1,len(rows_1)):
    #print(rows_1[i]) for astar
    if rows_1[i][6]==1:
        astar_no_of_success[no_of_nodes.index(rows_1[i][0])]+=1
        astar_no_of_generated_nodes[no_of_nodes.index(rows_1[i][0])]+=rows_1[i][8]
        astar_no_of_success_m[int(rows_1[i][1]-rows_1[i][2])]+=1
        astar_no_of_success_n_cont_2[no_of_success_n_cont_1.index(int(rows_1[i][5]))]+=1
        astar_no_of_success_hc_1[no_of_success_hc.index(int(rows_1[i][4]))]+=1
        
        astar_no_of_moves[no_of_nodes.index(rows_1[i][0])]+=rows_1[i][9]
        astar_no_of_moves_m[int(rows_1[i][1]-rows_1[i][2])]+=rows_1[i][9]
        astar_no_of_moves_mc[no_of_success_n_cont_1.index(int(rows_1[i][5]))]+=rows_1[i][9]
        astar_no_of_moves_hc[no_of_success_hc.index(int(rows_1[i][4]))]+=rows_1[i][9]
    #print(rows_1[i]) for dmh
    if rows_1[i][10]==1:
        dmh_no_of_success[no_of_nodes.index(rows_1[i][0])]+=1
        dmh_no_of_success_m[int(rows_1[i][1]-rows_1[i][2])]+=1
        dmh_no_of_success_n_cont_2[no_of_success_n_cont_1.index(int(rows_1[i][5]))]+=1
        dmh_no_of_success_hc_1[no_of_success_hc.index(int(rows_1[i][4]))]+=1
        
        dmh_no_of_moves[no_of_nodes.index(rows_1[i][0])]+=rows_1[i][12]
        dmh_no_of_moves_m[int(rows_1[i][1]-rows_1[i][2])]+=rows_1[i][12]
        dmh_no_of_moves_mc[no_of_success_n_cont_1.index(int(rows_1[i][5]))]+=rows_1[i][12]
        dmh_no_of_moves_hc[no_of_success_hc.index(int(rows_1[i][4]))]+=rows_1[i][12]
    #print(rows_1[i]) for idmh
    if rows_1[i][13]==1:
        idmh_no_of_success[no_of_nodes.index(rows_1[i][0])]+=1
        idmh_no_of_success_m[int(rows_1[i][1]-rows_1[i][2])]+=1
        idmh_no_of_success_n_cont_2[no_of_success_n_cont_1.index(int(rows_1[i][5]))]+=1
        idmh_no_of_success_hc_1[no_of_success_hc.index(int(rows_1[i][4]))]+=1
        
        idmh_no_of_moves[no_of_nodes.index(rows_1[i][0])]+=rows_1[i][15]
        idmh_no_of_moves_m[int(rows_1[i][1]-rows_1[i][2])]+=rows_1[i][15]
        idmh_no_of_moves_mc[no_of_success_n_cont_1.index(int(rows_1[i][5]))]+=rows_1[i][15]
        idmh_no_of_moves_hc[no_of_success_hc.index(int(rows_1[i][4]))]+=rows_1[i][15]
#print(astar_no_of_success)
for i in range(len(astar_no_of_success)):
    astar_no_of_success_u.append(astar_no_of_success[i]/48)
    dmh_no_of_success_u.append(dmh_no_of_success[i]/48)
    idmh_no_of_success_u.append(dmh_no_of_success[i]/48)
    
for i in range(len(astar_no_of_success_m)):
    #after filling form uncomment this
    """
    astar_no_of_moves[i]/=astar_no_of_success[i]
    astar_no_of_moves_m[i]/=astar_no_of_success_m[i]
    astar_no_of_moves_mc[i]/=astar_no_of_success_n_cont_2[i]
    """
    astar_no_of_success_m[i]/=48
    astar_no_of_success_n_cont_2[i]/=48
    
    dmh_no_of_moves_m[i]/=dmh_no_of_success_m[i]
    dmh_no_of_moves_mc[i]/=dmh_no_of_success_n_cont_2[i]
    dmh_no_of_success_m[i]/=48
    dmh_no_of_success_n_cont_2[i]/=48
    
    idmh_no_of_moves_m[i]/=idmh_no_of_success_m[i]
    idmh_no_of_success_m[i]/=48
    idmh_no_of_moves_mc[i]/=idmh_no_of_success_n_cont_2[i]
    idmh_no_of_success_n_cont_2[i]/=48

    

    dmh_no_of_moves[i]/=dmh_no_of_success[i]
    idmh_no_of_moves[i]/=idmh_no_of_success[i]

    
for i in range(len(no_of_success_hc)):
    #after filling form uncomment this
    """
    astar_no_of_moves_hc[i]/=astar_no_of_success_hc_1[i]
    """
    astar_no_of_success_hc_1[i]/=64

    dmh_no_of_moves_hc[i]/=dmh_no_of_success_hc_1[i]
    dmh_no_of_success_hc_1[i]/=64
    
    idmh_no_of_moves_hc[i]/=idmh_no_of_success_hc_1[i]
    idmh_no_of_success_hc_1[i]/=64
    
    

#a* success and search tree size
plt.figure(figsize=(16,12))
plt.suptitle("A*",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
plt.xlabel("No.of Clients")
plt.ylabel("NO.of Success")
plt.plot(no_of_nodes,astar_no_of_success,marker='d')

plt.title("Success rate Performance of astar algorithm")

#Plot 2

plt.subplot(2,2,2)
plt.xlabel("No.of Clients")
plt.ylabel("No.of generated nodes")
plt.plot(no_of_nodes,astar_no_of_generated_nodes,marker='d')

plt.title("Search tree size of astar algorithm")



#performance of a*
plt.figure(figsize=(25,12))
plt.suptitle("A*",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
#plt.xlabel("n")
plt.ylabel("UM/UMax")
plt.plot(no_of_nodes,astar_no_of_success_u,marker='*')

plt.title("Mean no.of success for a* for various n values")

#Plot 2

plt.subplot(2,2,2)
#plt.xlabel("m")
plt.ylabel("UM/UMax")
plt.plot(no_of_success_m1,astar_no_of_success_m,marker='d')

plt.title("Mean no.of success for a* for various m values")

#Plot 3

plt.subplot(2,2,3)
#plt.xlabel("mc")
plt.ylabel("UM/UMax")
plt.plot(no_of_success_n_cont,astar_no_of_success_n_cont_2,marker='d')

plt.title("Mean no.of success for a* for various mc values")

#Plot 4

plt.subplot(2,2,4)

plt.plot(no_of_success_hc,astar_no_of_success_hc_1,marker='d')
#plt.xlabel("hc")
plt.ylabel("UM/UMax")
plt.title("Mean no.of success for a* for various hc values")

#plt.show()

#performance of dmh
plt.figure(figsize=(20,12))
plt.suptitle("DMH",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
#plt.xlabel("n")
plt.ylabel("UM/UMax")
plt.plot(no_of_nodes,dmh_no_of_success_u,marker='*')

plt.title("Mean no.of success for DMH for various n values")

#Plot 2

plt.subplot(2,2,2)
#plt.xlabel("m")
plt.ylabel("UM/UMax")
plt.plot(no_of_success_m1,dmh_no_of_success_m,marker='d')

plt.title("Mean no.of success for DMH for various m values")

#Plot 3

plt.subplot(2,2,3)
#plt.xlabel("mc")
plt.ylabel("UM/UMax")
plt.plot(no_of_success_n_cont,dmh_no_of_success_n_cont_2,marker='d')

plt.title("Mean no.of success for DMH for various mc values")

#Plot 4

plt.subplot(2,2,4)

plt.plot(no_of_success_hc,dmh_no_of_success_hc_1,marker='d')
#plt.xlabel("hc")
plt.ylabel("UM/UMax")
plt.title("Mean no.of success for DMH for various hc values")

#performance of idmh
plt.figure(figsize=(20,12))
plt.suptitle("IDMH",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
#plt.xlabel("n")
plt.ylabel("UM/UMax")
plt.plot(no_of_nodes,idmh_no_of_success_u,marker='*')

plt.title("Mean no.of success for IDMH for various n values")

#Plot 2

plt.subplot(2,2,2)
#plt.xlabel("m")
plt.ylabel("UM/UMax")
plt.plot(no_of_success_m1,idmh_no_of_success_m,marker='d')

plt.title("Mean no.of success for IDMH for various m values")

#Plot 3

plt.subplot(2,2,3)
#plt.xlabel("mc")
plt.ylabel("UM/UMax")
plt.plot(no_of_success_n_cont,idmh_no_of_success_n_cont_2,marker='d')

plt.title("Mean no.of success for IDMH for various mc values")

#Plot 4

plt.subplot(2,2,4)
plt.ylim(-0.2,1.2)
plt.plot(no_of_success_hc,idmh_no_of_success_hc_1,marker='d')
#plt.xlabel("hc")
plt.ylabel("UM/UMax")
plt.title("Mean no.of success for IDMH for various hc values")



#Quality performance of a*
plt.figure(figsize=(25,12))
plt.suptitle("A* Quality",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
#plt.xlabel("n")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_nodes,astar_no_of_moves,marker='*')

plt.title("Mean no.of moves for a* for various n values")
#Plot 2

plt.subplot(2,2,2)
#plt.xlabel("m")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_success_m1,astar_no_of_moves_m,marker='d')

plt.title("Mean no.of moves for a* for various m values")

#Plot 3

plt.subplot(2,2,3)
#plt.xlabel("mc")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_success_n_cont,astar_no_of_moves_mc,marker='d')

plt.title("Mean no.of moves for a* for various mc values")

#Plot 4

plt.subplot(2,2,4)

plt.plot(no_of_success_hc,astar_no_of_moves_hc,marker='d')
#plt.xlabel("hc")
plt.ylabel("Mean(Zm)")
plt.title("Mean no.of moves for a* for various hc values")


#Quality performance of DMH
plt.figure(figsize=(25,12))
plt.suptitle("DMH Quality",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
#plt.xlabel("n")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_nodes,dmh_no_of_moves,marker='*')

plt.title("Mean no.of moves for dmh for various n values")
#Plot 2

plt.subplot(2,2,2)
#plt.xlabel("m")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_success_m1,dmh_no_of_moves_m,marker='d')

plt.title("Mean no.of moves for dmh for various m values")

#Plot 3

plt.subplot(2,2,3)
#plt.xlabel("mc")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_success_n_cont,dmh_no_of_moves_mc,marker='d')

plt.title("Mean no.of moves for dmh for various mc values")

#Plot 4

plt.subplot(2,2,4)

plt.plot(no_of_success_hc,dmh_no_of_moves_hc,marker='d')
#plt.xlabel("hc")
plt.ylabel("Mean(Zm)")
plt.title("Mean no.of moves for dmh for various hc values")


#Quality performance of IDMH
plt.figure(figsize=(25,12))
plt.suptitle("IDMH Quality",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
#plt.xlabel("n")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_nodes,idmh_no_of_moves,marker='*')

plt.title("Mean no.of moves for idmh for various n values")
#Plot 2

plt.subplot(2,2,2)
#plt.xlabel("m")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_success_m1,idmh_no_of_moves_m,marker='d')

plt.title("Mean no.of moves for idmh for various m values")

#Plot 3

plt.subplot(2,2,3)
#plt.xlabel("mc")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_success_n_cont,idmh_no_of_moves_mc,marker='d')

plt.title("Mean no.of moves for idmh for various mc values")

#Plot 4

plt.subplot(2,2,4)

plt.plot(no_of_success_hc,idmh_no_of_moves_hc,marker='d')
#plt.xlabel("hc")
plt.ylabel("Mean(Zm)")
plt.title("Mean no.of moves for idmh for various hc values")

#Likitha, add from this......
#for common graphs(merged)
#performance of a*, dmh and idmh
plt.figure(figsize=(25,12))
plt.suptitle("A*, DMH, IDMH",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
#plt.xlabel("n")
plt.ylabel("UM/UMax")
plt.plot(no_of_nodes,astar_no_of_success_u,marker='*',label="A*")
plt.plot(no_of_nodes,dmh_no_of_success_u,marker='*',label="DMH")
plt.plot(no_of_nodes,idmh_no_of_success_u,marker='*',label="IDMH")
plt.title("Mean no.of success for various n values")
plt.legend(loc='best')

#Plot 2

plt.subplot(2,2,2)
#plt.xlabel("m")
plt.ylabel("UM/UMax")
plt.plot(no_of_success_m1,astar_no_of_success_m,marker='d',label="A*")
plt.plot(no_of_success_m1,dmh_no_of_success_m,marker='d',label="DMH")
plt.plot(no_of_success_m1,idmh_no_of_success_m,marker='d',label="IDMH")
plt.title("Mean no.of success for various m values")
plt.legend(loc='best')

#Plot 3

plt.subplot(2,2,3)
#plt.xlabel("mc")
plt.ylabel("UM/UMax")
plt.plot(no_of_success_n_cont,astar_no_of_success_n_cont_2,marker='d',label="A*")
plt.plot(no_of_success_n_cont,dmh_no_of_success_n_cont_2,marker='d',label="DMH")
plt.plot(no_of_success_n_cont,idmh_no_of_success_n_cont_2,marker='d',label="IDMH")
plt.title("Mean no.of success for various mc values")
plt.legend(loc='best')

#Plot 4

plt.subplot(2,2,4)

plt.plot(no_of_success_hc,astar_no_of_success_hc_1,marker='d',label="A*")
plt.plot(no_of_success_hc,dmh_no_of_success_hc_1,marker='d',label="DMH")
plt.plot(no_of_success_hc,idmh_no_of_success_hc_1,marker='d',label="IDMH")
#plt.xlabel("hc")
plt.ylabel("UM/UMax")
plt.title("Mean no.of success for various hc values")
plt.legend(loc='best')



#Quality performance of a*, dmh and idmh
plt.figure(figsize=(25,12))
plt.suptitle("A* Quality, DMH Quality and IDMH Quality",fontsize=16)
#Plot 1

plt.subplot(2,2,1)
#plt.xlabel("n")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_nodes,astar_no_of_moves,marker='*',label="A*")
plt.plot(no_of_nodes,dmh_no_of_moves,marker='*',label="DMH")
plt.plot(no_of_nodes,idmh_no_of_moves,marker='*',label="IDMH")
plt.title("Mean no.of moves for various n values")
plt.legend(loc='best')
#Plot 2

plt.subplot(2,2,2)
#plt.xlabel("m")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_success_m1,astar_no_of_moves_m,marker='d',label="A*")
plt.plot(no_of_success_m1,dmh_no_of_moves_m,marker='d',label="DMH")
plt.plot(no_of_success_m1,idmh_no_of_moves_m,marker='d',label="IDMH")
plt.title("Mean no.of moves for various m values")
plt.legend(loc='best')

#Plot 3

plt.subplot(2,2,3)
#plt.xlabel("mc")
plt.ylabel("Mean(Zm)")
plt.plot(no_of_success_n_cont,astar_no_of_moves_mc,marker='d',label="A*")
plt.plot(no_of_success_n_cont,dmh_no_of_moves_mc,marker='d',label="DMH")
plt.plot(no_of_success_n_cont,idmh_no_of_moves_mc,marker='d',label="IDMH")
plt.title("Mean no.of moves for various mc values")
plt.legend(loc='best')

#Plot 4

plt.subplot(2,2,4)

plt.plot(no_of_success_hc,astar_no_of_moves_hc,marker='d',label="A*")
plt.plot(no_of_success_hc,dmh_no_of_moves_hc,marker='d',label="DMH")
plt.plot(no_of_success_hc,idmh_no_of_moves_hc,marker='d',label="IDMH")
#plt.xlabel("hc")
plt.ylabel("Mean(Zm)")
plt.title("Mean no.of moves for various hc values")
plt.legend(loc='best')

#Likitha, upto this.........



plt.show()

