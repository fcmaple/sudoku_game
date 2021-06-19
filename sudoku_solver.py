board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
lst = []
def valid(bo,x,y):
   for i in range(9):
        if (i!=y and bo[x][i] == bo[x][y] )or bo[x][y]==0:
            return False
   for i in range(9):
        if (i!=x and bo[i][y] == bo[x][y])or bo[x][y]==0:
            return False
   #print(x,y)
   return True
           

def print_board(bo):
    for i in range(len(bo)):
        if i%3 ==0 and i!=0:
            print("---------")
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print("|",end ='')
            if j==8:
                print(bo[i][j])
            else:
                print(bo[i][j],end='')
                
                
def find_empty(bo):
    i= 0
    j=0
    value = 0
    while(i<len(bo)):
        while(j<len(bo[0])):
            if bo[i][j] == 0:
                value=0
                while(solve(bo,i,j,value) == False):
                    bo[i][j]=0
                    tmp = lst.pop()
                    #print('tmp',tmp)
                    i = tmp[0]
                    j = tmp[1]
                    value = tmp[2]+1
                
            j=j+1
        i=i+1
        j=0
    return False;

def solve(bo,x,y,v):
    #print(x,y,v)
    i = v
    while (i < 10):
        bo[x][y] = i
        #print(x,y,i)
        if(valid(bo,x,y)==True):
            print(print_board(bo))
            lst.append((x,y,i))
            #print(lst)
            return True
        i=i+1
    return False
def solve_all(bo):
    find = find_empty(bo)
    if find == False:
        return True




        
        
        
        