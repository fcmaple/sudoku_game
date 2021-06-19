import pygame
import time
pygame.font.init()

class Grid:
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
    def __init__(self,col,row,height,width,win):#just a grid no value
        self.col = col
        self.row = row
        self.height = height
        self.width = width
        self.cube = [[Cube(self.board[i][j],i,j,height,width)for i in range(col)]for j in range(row)]
        self.update_model()
        self.win = win
        self.selected = None
    
    def set_problem(self):
        for i in range(self.row):
            for j in range(self.col):
                if(self.board[i][j]!=0):
                    self.cube[i][j].value = self.board[i][j]
        for i in range(self.row):
            print("\n")
            for j in range(self.col):
                print(self.cube[i][j].value,end=' ')
        
    def update_model(self):
       self.model = [[self.cube[i][j].value for i in range(self.col)] for j in range(self.row)]
       print(self.model)
    def click(self,pos):
        
        #print(self.width,self.height)
        gap = self.width/9
        x  = pos[0]//gap
        y  = pos[1]//gap
        if self.selected:
            pygame.draw.rect(self.win,(0,0,0),(self.selected[0]*gap,self.selected[1]*gap,gap,gap),1)
        if pos[0] <self.height and pos[1]<self.width:
            
            pygame.draw.rect(self.win,(255,0,0),(x*gap,y*gap,gap,gap),3)
            print((int(x),int(y)))
            return (int(x),int(y))
        else:
            return None
    def select(self,xx,yy):
        for i in range(self.row):
            for j in range(self.col):
                self.cube[i][j].selected = False;
        self.cube[xx][yy].selected = True
        self.selected = (xx,yy)
        #print(self.cube[xx][yy].value)
        return
    def valid(self,x,y,val):
        for i in range(self.row):
            if self.cube[i][y].value == val:
                return False
            if self.cube[x][i].value == val:
                return False
        #print("success",x,y,val)
        return True
    def place(self,x,y,val):#先檢查，ok後再擺放
        if self.valid(x,y,val):
            self.cube[x][y].value = val
            self.cube[x][y].clean(self.win)
            self.cube[x][y].draw_change(self.win)
        else:
            self.clean_choice()
    def clean_choice(self):
        
        x = self.selected[0]
        y = self.selected[1]
        gap = self.width/9
        pygame.draw.rect(self.win,(255,255,255),(x*gap,y*gap,gap,gap),3)#先塗白
        self.cube[x][y].clean(self.win)
        
        #在全部重塗過
        for i in range(9):# row有幾個
            if i%3==0 and i!=0:
                think = 4
            else :
                think = 1
            pygame.draw.line(self.win,(0,0,0),(0,i*gap),(self.height,i*gap),think)
            pygame.draw.line(self.win,(0,0,0),(i*gap,0),(i*gap,self.width),think)
    def show(self):
        gap = self.width /9

        for i in range(9):# row有幾個
            if i%3==0 and i!=0:
                think = 4
            else :
                think = 1
            pygame.draw.line(self.win,(0,0,0),(0,i*gap),(self.height,i*gap),think)
            pygame.draw.line(self.win,(0,0,0),(i*gap,0),(i*gap,self.width),think)
        for i in range(self.row):
           
            for j in range(self.col):
                self.cube[i][j].draw(self.win)
    def success(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.cube[i][j].value ==0:
                    return False
        return True
    def solve(self,x,y,val):
        
        
        i=val
        while(i<10):
            if(self.valid(x,y,i)==True):
                #print("valid")
                self.lst.append((x,y,i))
                #print(self.lst)
                self.cube[x][y].set(i)
                #print("set",x,y,i)
                self.cube[x][y].draw(self.win)
                pygame.display.update()
                pygame.time.delay(10)
                return True
            i=i+1
        return False
    def find_empty(self):
        i=0
        j=0
        value = 0
        while(j<self.row):
            while(i<self.col):
                if (self.cube[i][j].value==0):
                    value = 0
                    print(i,j,value)
                    while(self.solve(i,j,value)==False):
                        tmp = self.lst.pop()
                        i = tmp[0]
                        j = tmp[1]
                        value = tmp[2]+1
                        self.cube[i][j].set(0)
                        self.cube[i][j].draw(self.win)
                        pygame.display.update()
                        pygame.time.delay(10)
                        #print("tmp ",i,j,value)
                i=i+1
            j=j+1
            i=0
        return False

    def solve_problem(self):
        find = self.find_empty() 
        if find ==False:
            return True
       
     
                
            
    
        
class Cube:
    row = 9
    col = 9
    
    def __init__(self,value,row,col,height,width):
        self.value = value
        self.row = row
        self.col = col
        self.height = height
        self.width = width
        self.temp = 0
        self.selected = False #被選到
    def draw(self,win):
        fnt = pygame.font.SysFont("comicsans",40)
        gap = self.width /9 #每一間格
        x = self.col*gap
        y = self.row*gap
        if self.temp!=0 and self.value ==0: #如果暫時沒填字則有灰色
            text = fnt.render(str(self.temp),1,(128,128,128))
            win.blit(text,(x+5,y+5))
        elif self.value==0 and self.temp ==0 :
            pygame.draw.rect(win,(255,255,255),(x+10,y+10,gap-20,gap-20),0)
        elif self.value!=0 and self.temp==0:
            text = fnt.render(str(self.value),1,(0,0,0))#自行顏色
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
        if self.selected: #?
            pygame.draw.rect(win,(255,0,0),(x,y,gap,gap),3)#選到的格子畫紅色
    def draw_change(self,win,g= True):
        fnt = pygame.font.SysFont("comicsans",40)
        gap = self.width /9
        x = self.col*gap
        y = self.row*gap
        pygame.draw.rect(win,(255,255,255),(x,y,gap,gap),0)#劃一格
        text = fnt.render(str(self.value),1,(0,0,0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win,(0,255,0),(x,y,gap,gap),3)
        else:
            pygame.draw.rect(win,(255,0,0),(x,y,gap,gap),3)
    def clean(self,win):
        gap = self.width /9 #每一間格
        x = self.col*gap
        y = self.row*gap
        if self.temp !=0 and self.value==0:
            pygame.draw.rect(win,(255,255,255),(x,y,gap,gap),0)
    def set(self,val):
        self.value = val
    def set_tmp(self,val):
        self.temp = val
def main():
    win = pygame.display.set_mode((540,600)) #背景
    pygame.display.set_caption("sudoku")
    board = Grid(9,9,540,540,win)
    win.fill((255,255,255))
    key = None
    run = True
    start = time.time()
    board.show()
    ##board.set_problem()
    while run:
        #play_time = round(time.time()-start)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key=1
                if event.key == pygame.K_2:
                    key=2
                if event.key == pygame.K_3:
                    key=3
                if event.key == pygame.K_4:
                    key=4
                if event.key == pygame.K_5:
                   key=5
                if event.key == pygame.K_6:
                   key=6
                if event.key == pygame.K_7:
                   key=7
                if event.key == pygame.K_8:
                   key=8
                if event.key == pygame.K_9:
                   key=9

                if event.key == pygame.K_SPACE:
                    board.solve_problem()
                    
                if event.key == pygame.K_RETURN:
                    print("enter")
                    i,j = board.selected
                    print("board,selected",i,j)
                    board.place(i,j,key)
                    key = 0
            if event.type ==  pygame.MOUSEBUTTONDOWN:
                if board.selected:
                    board.clean_choice()
                pos = pygame.mouse.get_pos()#找到座標
                print("pos",pos)
                clicked = board.click(pos)
                print("clicked",clicked)
                #print(type(clicked[1]))
                if clicked:
                    board.select(clicked[0],clicked[1])
                    key = None
            if key!=0 and key!=None  and board.selected != None: #temp -> gray
                board.cube[board.selected[0]][board.selected[1]].temp = key
                board.cube[board.selected[0]][board.selected[1]].draw(win)
        
        pygame.display.update()
        
main()
pygame.quit()        