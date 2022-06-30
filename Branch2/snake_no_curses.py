
import datetime
import random


class snake:
    
    ## координаты головы змеи
    x = 15 # left, right
    y = 15 # up, down


    scene = ''
    direction = '' 

    menu_lst=['    SNAKE ', 'Start new game', ' Top results  ', '     Exit     ']
    menu_item=1
    records_lst=[' Back ', ' Clear results ']
    records_item=0
    new_name=''

    robot_snake=False
    second_snake=False

    ### initiation
    def __init__(self):

        ## create matrix and a snake
        self.matrix = [[ 0 for i in range(30)] for _ in range(30)]
        self.snake_head = [[0]]
        self.snake_body={i:[self.x, self.y+i-1] for i in range(1, 8)}

        ## add borders
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i==0 or i==len(self.matrix)-1 or j==0 or j==len(self.matrix[i])-1:
                    self.matrix[i][j]=1

        self.direction = 'up'
        self.scene='menu'
        self.timer = datetime.datetime.now()
        self.rabbit()

    ### new game
    def initiation(self):
        self.x = 15
        self.y = 15
        self.direction = 'up'
        self.scene='game'
        self.snake_body={i:[self.x, self.y+i-1] for i in range(1, 8)}
        if self.second_snake==False:
            self.robot_snake=False
  
        self.delete_rabbits()



    ### has screen changed
    def has_screen_changed(self):

        pass











    ### draw
    def draw(self):
        pass














    ### changes direction of snake head
    def rotate_snake(self, command):     ### изменяет направление змеи
        new_x, new_y=self.x, self.y

        if command=='left' and self.direction!='right':
            if self.__can_move(new_x-1, new_y) == True:
                self.direction='left'

        elif command=='right' and self.direction!='left':
            if self.__can_move(new_x+1, new_y) == True:
                self.direction='right'

        elif command=='down' and self.direction!='up':
            if self.__can_move(new_x, new_y+1) == True:
                self.direction='down'

        elif command=='up' and self.direction!='down':
            if self.__can_move(new_x, new_y-1) == True:
                self.direction='up'

    ### changes x and y of snake head
    def move_head(self):
        if self.direction=='left':
            if self.__can_move(self.x-1, self.y):
                self.x-=1
        elif self.direction=='right':
            if self.__can_move(self.x+1, self.y):
             self.x+=1
        elif self.direction=='down':
            if self.__can_move(self.x, self.y+1):
             self.y+=1
        elif self.direction=='up':
            if self.__can_move(self.x, self.y-1):
                self.y-=1   

    ### move body//game over if head doesn't move//snake grow if eat rabbits
    def move_body(self):
        if self.matrix[self.y][self.x]==2:
            self.snake_body[len(self.snake_body)+1]=self.snake_body[len(self.snake_body)]
            self.rabbit()
        for i in range(len(self.snake_body), 1, -1):
            self.snake_body[i]=self.snake_body[i-1] 

        for i in range(2, len(self.snake_body)+1):
            if self.snake_body[i]==[self.x, self.y]: 
                self.scene='game over'
        self.snake_body[1]=[self.x, self.y]

    ### can move if 0 or rabbit//cant move back
    def __can_move(self, new_x, new_y): 
        if self.matrix[new_y][new_x]==0 or self.matrix[new_y][new_x]==2:
            if self.snake_body[2]==[new_x, new_y]:
                return False
            return True
        else:
            return False









    ### delete rabbits
    def delete_rabbits(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]==2:
                    self.matrix[i][j]=0

    ### generate rabbits
    def rabbit(self):
        if self.second_snake==False:
            self.delete_rabbits()
            y, x=random.randint(1, 28), random.randint(1, 28)
            for i in range(1, len(self.snake_body)+1):
                if self.snake_body[i]==[x, y]:
                    self.rabbit()
            self.matrix[5][15]=2
            if self.second_snake==True:
                self.delete_rabbits()
                self.matrix[y][x]=2





 ### pause
    def pause(self):
        pass


# find path
    def find_path(self, matrix): # -screen, self
        num_matrix = [[ 0 for i in range(30)] for _ in range(30)]


        # borders
        for l in range(len(matrix)):
                for j in range(len(matrix[l])):
                    if l==0 or l==len(matrix)-1 or j==0 or j==len(matrix[l])-1:
                        num_matrix[l][j]=999

        # rabbit
        for l in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[l][j]==2:
                    num_matrix[l][j]=998
                    end_x=j
                    end_y=l

        # snake body
        body=len(self.snake_body)//2
        for i in range(1, len(self.snake_body)+1):
            if self.snake_body[i][1]>=self.y and body>(self.snake_body[i][1]-self.y): # down
                num_matrix[self.snake_body[i][1]][self.snake_body[i][0]]=999

            if self.snake_body[i][1]<=self.y and body>(self.y-self.snake_body[i][1]): # up
                num_matrix[self.snake_body[i][1]][self.snake_body[i][0]]=999

            if self.snake_body[i][0]>=self.x and body>(self.snake_body[i][0]-self.x): # right
                num_matrix[self.snake_body[i][1]][self.snake_body[i][0]]=999

            if self.snake_body[i][0]<=self.x and body>(self.x-self.snake_body[i][0]): # left
                num_matrix[self.snake_body[i][1]][self.snake_body[i][0]]=999


        # snake head
        num_matrix[self.y][self.x]=1

        pathfound=False
        num=0



        ### проходим матрицу и заполняем её значениями дистанции от стартовой точки ###

        while pathfound == False:

            for l in range(1, len(num_matrix)-1):
                for j in range(1, len(num_matrix[l])-1):
                    if num_matrix[l][j]==998 or num_matrix[l][j]==0:
                        # надо определить, есть ли в ближайшем окружении заполненные ячейки, и, если есть, выбрать среди них наименьшую

                        found = False # если не найдено заполненых клеток
                        value=999


                        ## поиск клеток со значением больше 0; не стены
                        ## поиск наименьшего значения (расстояния от кролика)

                        # верхняя клетка
                        if num_matrix[l-1][j]<998 and num_matrix[l-1][j]>0: 
                            found=True
                            if num_matrix[l-1][j]<value and num_matrix[l-1][j]!=0: # поиск наименьшего значения 
                                value = num_matrix[l-1][j]

                        # нижняя клетка
                        if num_matrix[l+1][j]<998 and num_matrix[l+1][j]>0: 
                            found=True
                            if num_matrix[l+1][j]<value: # поиск наименьшего значения 
                                value = num_matrix[l+1][j]

                        # левая клетка
                        if num_matrix[l][j-1]<998 and num_matrix[l][j-1]>0: 
                            found=True
                            if num_matrix[l][j-1]<value: # поиск наименьшего значения 
                                value = num_matrix[l][j-1]

                        # правая клетка
                        if num_matrix[l][j+1]<998 and num_matrix[l][j+1]>0: 
                            found=True
                            if num_matrix[l][j+1]<value: # поиск наименьшего значения 
                                value = num_matrix[l][j+1]


                        # проверить если путь найден
                        if end_y==l and end_x==j and found==True:
                            pathfound=True

                        # увеличить значение в центральной клетке до наименьшего+1
                        if found==True and value<num and num_matrix[l][j]==0:
                            num_matrix[l][j]=value+1

            num+=1

        
        # numbered matrix, end x, end y >>>> path
        # path lenght = num
        path, j, l= {}, end_x, end_y


        for i in range(num-2, 0, -1):

            a = [] # список значений из numbered matrix
            b = [] # список соответствующих им координат
 

            if num_matrix[l - 1][j] >1 and num_matrix[l - 1][j] < 999: # up
                a.append(num_matrix[l - 1][j])
                b.append([l - 1, j])

            if num_matrix[l + 1][j] >1 and num_matrix[l + 1][j] < 999: # down

                a.append(num_matrix[l + 1][j])
                b.append([l + 1, j])

            if num_matrix[l][j - 1] >1 and num_matrix[l][j - 1] < 999: # left
                a.append(num_matrix[l][j - 1])
                b.append([l, j - 1])

            if num_matrix[l][j + 1] >1 and num_matrix[l][j + 1] < 999: # right
                a.append(num_matrix[l][j + 1])
                b.append([l, j + 1])

            ###
            if num_matrix[l][j]>1 and num_matrix[l][j]<999:
                a.append(num_matrix[l][j])
                b.append([l, j])


            path[i] = b[a.index(min(a))]
            l = b[a.index(min(a))][0]
            j = b[a.index(min(a))][1]  
        if len(path)==0:
            path[1]=[end_y, end_x]


        #txt robot snake path
        f=open('robot_snake_path.txt', 'a')
        f.write('\n'+str(datetime.datetime.now())+'\n'+'\n')
        f.write('\n'+str(path)+'\n')
        for i in num_matrix:
            f.write(str(i)+'\n')

        return path



    ### auto snake
    def auto_move_snake(self):
        path=self.find_path(self.matrix)
        if path[1][1]<self.x:
            if self.direction!='right':
                self.rotate_snake('left')
            else:
                self.rotate_snake('down')
        elif path[1][1]>self.x:
            if self.direction!='left':
                self.rotate_snake('right')
            else:
                self.rotate_snake('up')
        elif path[1][0]<self.y:
            if self.direction!='down':
                self.rotate_snake('up')
            else:
                self.rotate_snake('left')
        elif path[1][0]>self.y:
            if self.direction!='up':
                self.rotate_snake('down')
            else:
                self.rotate_snake('right')

    ### tick
    def tick(self):         ### двигает змею
        if self.scene == 'game':
            if (datetime.datetime.now()-self.timer).microseconds>=290000:
                self.timer=datetime.datetime.now()
                self.move_head()
                self.move_body()
            if self.robot_snake==True:
                self.auto_move_snake()


    ### get input
    def getinput(self):
        self.scene='game'
        self.robot_snake=True







def run_game():
    while True:
        snake1.getinput()
        snake1.draw()
        snake1.tick()
        


snake1 = snake()


#txt robot snake2 path
f = open('robot_snake_path.txt', 'w')
f.write(' ')
f.close()


run_game()













