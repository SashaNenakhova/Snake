import curses
import datetime
import random

from draw_snake_game import *               #draw, draw_menu, draw_game
from move_snake import *                    #rotate_snake, move_head, move_body, __can_move, auto_move_snake
from records_functions import *             #update_file, read_file, add_records, clear_records
from get_input import *                     #getinput


# class snake:
    
#     ## координаты головы змеи
#     x = 15 # left, right
#     y = 15 # up, down

#     screen = None

#     scene = ''
#     direction = '' 

#     menu_lst=['    SNAKE ', 'Start new game', ' Top results  ', '     Exit     ']
#     menu_item=1
#     records_lst=[' Back ', ' Clear results ']
#     records_item=0
#     new_name=''
#     rotate_keys=[0, 0]

#     top_corner=0
#     left_corner=0
#     num=0
#     path={}

#     snakes_list=[]
#     robot_snake=False
#     second_snake=False
#     deadcount=0



#     wave_algorithm=False



#     steps_count=0 ##################### statistic #################################
#     counting=False
#     timer2=0
#     count_time=0



#     ### initiation
#     def __init__(self):
#         screen = None

#         ## create matrix and a snake
#         self.matrix = [[ 0 for i in range(40)] for _ in range(40)]
#         self.snake_head = [[0]]

#         if self.second_snake==True:
#             self.x=20
#             self.snake_body={i:[self.x, self.y] for i in range(1, 8)}
#         else:
        
#             self.snake_body={i:[self.x, self.y+i-1] for i in range(1, 8)}
#             self.scene='menu'
#             self.records_top=read_file(self)

#         ## add borders
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[i])):
#                 if i==0 or i==len(self.matrix)-1 or j==0 or j==len(self.matrix[i])-1:
#                     self.matrix[i][j]=1

#         self.direction = 'up'
#         self.timer = datetime.datetime.now()


#     ### new game
#     def initiation(self):
#         if self.second_snake==True:
#             self.x, self.y=random.randint(1, 28), random.randint(1, 28)
#             self.snake_body={i:[self.x, self.y] for i in range(1, 8)}

#         else:
#             self.x = 15        
#             self.y = 15


#             self.matrix = [[ 0 for i in range(40)] for _ in range(40)]
#             ## add borders
#             for i in range(len(self.matrix)):
#                 for j in range(len(self.matrix[i])):
#                     if i==0 or i==len(self.matrix)-1 or j==0 or j==len(self.matrix[i])-1:
#                         self.matrix[i][j]=1


#             self.robot_snake=True ################ STATISTIC ######################
#             self.snake_body={i:[self.x, self.y+i-1] for i in range(1, 15)}
#             self.snakes_list=[snake1]


#             self.find_path_x, self.find_path_y=0, 0 ########################

#         self.num_matrix= [[ 0 for i in range(40)] for _ in range(40)]
#         self.num=0

#         self.direction = 'up'
#         self.scene='game'
        



#     ### has screen changed
#     def has_screen_changed(self):

#         current_dimensions = self.screen.getmaxyx()

#         ## terminal too small
#         while self.screen.getmaxyx()[0]<len(self.matrix)+4 or self.screen.getmaxyx()[1]<len(self.matrix[0])*2+3:
#             current_dimensions = self.screen.getmaxyx()
            
#             ## exit
#             key=self.screen.getch()
#             if key==ord('q'):
#                 self.screen.clear()
#                 exit(0)

#             ## screen has changed
#             if self.screen_dimensions != current_dimensions:
#                 self.screen_dimensions = current_dimensions
#                 self.screen.clear()

#             ## terminal too small
#             if self.screen.getmaxyx()[0]<len(self.matrix)+4 or self.screen.getmaxyx()[1]<len(self.matrix[0])*2+3:
#                 self.screen.move(self.screen.getmaxyx()[0]//2, self.screen.getmaxyx()[1]//2-9)
#                 self.screen.addstr('Terminal too small', curses.color_pair(16))
#             elif self.screen.getmaxyx()[0]<3 or self.screen.getmaxyx()[1]<20:
#                 self.screen.move(self.screen.getmaxyx()[0]//2, self.screen.getmaxyx()[1]//2-3)
#                 self.screen.addstr('Error', curses.color_pair(16))
#             else:
#                 self.screen.addstr(0, 0, ' ')

#         ## screen has changed
#         if current_dimensions != self.screen_dimensions:
#             self.screen_dimensions = current_dimensions
#             self.screen.clear()












#     ### delete rabbits
#     def delete_rabbit(self, x, y):
#         snake1.matrix[y][x]=0

#     ### generate rabbits
#     def rabbit(self):
#         # self.delete_rabbits()

#         if self.second_snake==False:

#             y, x=random.randint(1, 28), random.randint(1, 28)

#             if self.matrix[y][x]==1: # если стена
#                 self.rabbit()
#             else:
#                 self.matrix[y][x]=2


#             for i in snake1.snakes_list: # если змея
#                 for j in range(1, len(i.snake_body)+1):
#                     if i.snake_body[j]==[x, y]:
#                         self.delete_rabbit(x, y)
#                         self.rabbit()
        

#         else:

#             for i in range(1, len(self.snake_body)+1):     
#                 if self.snake_body[i]==[x, y]:
#                     # snake1.rabbit()
#                     snake1.delete_rabbit(x, y)

#             for i in range(len(snake1.matrix)):
#                 for j in range(len(snake1.matrix[i])):
#                     if snake1.matrix[i][j]==2:
#                         self.matrix[y][x]=2


#  ### pause
#     def pause(self):
#         self.screen.nodelay(False)

#         key=0
#         while True:
#             box = curses.newwin(3, 10, self.screen.getmaxyx()[0]//2, self.screen.getmaxyx()[1]//2)
#             box.box()
#             box.bkgd(' ', curses.color_pair(16))    
#             box.addstr(1, 2, 'Paused', curses.color_pair(16))
#             box.refresh()

#             key=self.screen.getch()
#             if key==ord('p') or key==ord('P'):
#                 break

#             draw(self)

#         box.bkgd(' ', curses.color_pair(0))
#         box.clear()
#         box.refresh()

#         self.screen.nodelay(True)


































































def path_not_found(self):

    self.num_matrix[self.y][self.x]=1###

    num=0
    while num<30:

        for l in range(1, len(self.num_matrix)-1):
            for j in range(1, len(self.num_matrix[l])-1):
                if self.num_matrix[l][j]==998 or self.num_matrix[l][j]==0:
                    # надо определить, есть ли в ближайшем окружении заполненные ячейки, и, если есть, выбрать среди них наименьшую

                    found = False # если не найдено заполненых клеток
                    value=999


                    ## поиск клеток со значением больше 0; не стены
                    ## поиск наименьшего значения (расстояния от кролика)

                    # верхняя клетка
                    if self.num_matrix[l-1][j]<998 and self.num_matrix[l-1][j]>0: 
                        found=True
                        if self.num_matrix[l-1][j]<value: # поиск наименьшего значения 
                            value = self.num_matrix[l-1][j]

                    # нижняя клетка
                    if self.num_matrix[l+1][j]<998 and self.num_matrix[l+1][j]>0: 
                        found=True
                        if self.num_matrix[l+1][j]<value: # поиск наименьшего значения 
                            value = self.num_matrix[l+1][j]

                    # левая клетка
                    if self.num_matrix[l][j-1]<998 and self.num_matrix[l][j-1]>0: 
                        found=True
                        if self.num_matrix[l][j-1]<value: # поиск наименьшего значения 
                            value = self.num_matrix[l][j-1]

                    # правая клетка
                    if self.num_matrix[l][j+1]<998 and self.num_matrix[l][j+1]>0: 
                        found=True
                        if self.num_matrix[l][j+1]<value: # поиск наименьшего значения 
                            value = self.num_matrix[l][j+1]



                    # увеличить значение в центральной клетке до наименьшего+1
                    # if found==True and value<snake1.num and snake1.num_matrix[l][j]==0:
                    if found==True and value<self.num and self.num_matrix[l][j]==0:
                        self.num_matrix[l][j]=value+1
        num+=1



    self.num_matrix[self.y][self.x]=998 ###
































#### numbered matrix
def wave3(self):

    # aaa
    for i in snake1.snakes_list:
        i.wave_algorithm=False

    # rabbit
    for l in range(len(snake1.matrix)):
        for j in range(len(snake1.matrix)):
            if snake1.matrix[l][j]==2:
                snake1.num_matrix[l][j]=1

    # snake body
    steps=0
    a1, b1=0, 0
    snake_body=0 
    for i in snake1.snakes_list:
        snake_body=i.snake_body  
        for j in range(1, len(snake_body)+1):
            if snake_body[j][1]>self.y: # расстояние y
                a1=snake_body[j][1]-self.y 
            else:
                a1=self.y-snake_body[j][1] 
            if snake_body[j][0]>self.x: # расстояние x
                b1=snake_body[j][0]-self.x 
            else:
                b1=self.x-snake_body[j][0] 
            steps=len(snake_body)+1-j # через сколько шагов хвост пропадет
            if steps>=a1 and steps>=b1:
                self.num_matrix[snake_body[j][1]][snake_body[j][0]]=999  
            self.num_matrix[i.y][i.x]=998### 

    # snake head
    self.num_matrix[self.y][self.x]=998
    end_x=self.x
    end_y=self.y

    # borders
    for l in range(len(snake1.matrix)):
        for j in range(len(snake1.matrix[l])):
            if snake1.matrix[l][j]==1:
                snake1.num_matrix[l][j]=999

    for i in snake1.snakes_list:
        snake1.num_matrix[i.y][i.x]=998

    pathfound=False
    pathnotfound=False
    snake1.num=0

    ### проходим матрицу и заполняем её значениями дистанции от стартовой точки ###
    while pathfound == False:

        for l in range(1, len(snake1.num_matrix)-1):
            for j in range(1, len(snake1.num_matrix[l])-1):
                if snake1.num_matrix[l][j]==998 or snake1.num_matrix[l][j]==0:
                    # надо определить, есть ли в ближайшем окружении заполненные ячейки, и, если есть, выбрать среди них наименьшую

                    found = False # если не найдено заполненых клеток
                    value=999


                    ## поиск клеток со значением больше 0; не стены
                    ## поиск наименьшего значения (расстояния от кролика)

                    # верхняя клетка
                    if snake1.num_matrix[l-1][j]<998 and snake1.num_matrix[l-1][j]>0: 
                        found=True
                        if snake1.num_matrix[l-1][j]<value: # поиск наименьшего значения 
                            value = snake1.num_matrix[l-1][j]

                    # нижняя клетка
                    if snake1.num_matrix[l+1][j]<998 and snake1.num_matrix[l+1][j]>0: 
                        found=True
                        # if snake1.num_matrix[l+1][j]<value: # поиск наименьшего значения 
                        if snake1.num_matrix[l+1][j]<value: # поиск наименьшего значения  
                            value = snake1.num_matrix[l+1][j]

                    # левая клетка
                    if snake1.num_matrix[l][j-1]<998 and snake1.num_matrix[l][j-1]>0: 
                        found=True
                        if snake1.num_matrix[l][j-1]<value: # поиск наименьшего значения 
                            value = snake1.num_matrix[l][j-1]

                    # правая клетка
                    if snake1.num_matrix[l][j+1]<998 and snake1.num_matrix[l][j+1]>0: 
                        found=True
                        if snake1.num_matrix[l][j+1]<value: # поиск наименьшего значения 
                            value = snake1.num_matrix[l][j+1]




                    # увеличить значение в центральной клетке до наименьшего+1
                    # if found==True and value<snake1.num and snake1.num_matrix[l][j]==0:
                    if found==True and value<snake1.num and snake1.num_matrix[l][j]==0:
                        snake1.num_matrix[l][j]=value+1




                    # проверить если путь найден
                    for i in snake1.snakes_list:
                        if l==i.y and j==i.x and found==True:
                        # if (snake1.num_matrix[i.y-1][i.x]>0 and snake1.num_matrix[i.y-1][i.x]<999) or (snake1.num_matrix[i.y+1][i.x]>0 and snake1.num_matrix[i.y+1][i.x]<999) or (snake1.num_matrix[i.y][i.x-1]>0 and snake1.num_matrix[i.y][i.x-1]<999) or (snake1.num_matrix[i.y][i.x+1]>0 and snake1.num_matrix[i.y][i.x+1]<999):
                            i.wave_algorithm=True
                            i.num=snake1.num

                    for i in snake1.snakes_list:
                        if i.wave_algorithm==False:
                            break
                    else:
                        pathfound=True
        snake1.num+=1
        if snake1.num>100:
            pathnotfound=True
            pathfound=True
    # на пути хвост
    # if pathnotfound==True:
    for i in snake1.snakes_list:
        if i.wave_algorithm!=True:
            i.path_not_found() ##################
    for i in snake1.snakes_list:
        i.wave_algorithm=False
    snake1.find_path_x, snake1.find_path_y=end_x, end_y























# find path
def find_path3(self): # -screen, self
    j, l=self.x, self.y ###

    # ### second snakes matrix (snakes bodies + snake1.num_matrix)
    if self!=snake1:
        for i in range(len(snake1.num_matrix)):
            for t in range(len(snake1.num_matrix[i])):
                if snake1.num_matrix[i][t]<999:
                    self.num_matrix[i][t]=snake1.num_matrix[i][t]
        # snake body
        steps=0
        a1, b1=0, 0
        snake_body=0 
        for i in snake1.snakes_list:
            snake_body=i.snake_body
            self.num_matrix[i.y][i.x]=998 ###   
            for k in range(1, len(snake_body)+1):
                if snake_body[k][1]>self.y: # расстояние y
                    a1=snake_body[k][1]-self.y
                else:
                    a1=self.y-snake_body[k][1]
                if snake_body[k][0]>self.x: # расстояние x
                    b1=snake_body[k][0]-self.x
                else:
                    b1=self.x-snake_body[k][0]
                steps=len(snake_body)+1-k # через сколько шагов хвост пропадет
                if steps>=a1 and steps>=b1:
                    self.num_matrix[snake_body[k][1]][snake_body[k][0]]=999

        self.num_matrix[self.y][self.x]=998####

        ##########
        for i in range(len(self.num_matrix)):
            for k in range(len(self.num_matrix[i])):
                if self.num_matrix[i][k]==2:
                    if self.x<=k:
                        self.num=k-self.x
                    else:
                        self.num=self.x-k
                    if self.y<=i:
                        self.num+=i-self.y
                    else:
                        self.num+=self.y-i
                
    if self!=snake1:
        f=open('robot_snake_path.txt', 'a')
        f.write(str(self.num)+'  num'+ '\n'*2)
    # numbered matrix, end x, end y >>>> path
    # path lenght = num
    # j, l= end_x, end_y
    path={}
    # for i in range(snake1.num-2, 0, -1):
    for i in range(1, self.num+1):

        a = [] # список значений из numbered matrix
        b = [] # список соответствующих им координат


        if self.num_matrix[l - 1][j] >0 and self.num_matrix[l - 1][j] < 998: # up
            a.append(self.num_matrix[l - 1][j])
            b.append([l - 1, j])

        if self.num_matrix[l + 1][j] >0 and self.num_matrix[l + 1][j] < 998: # down
            a.append(self.num_matrix[l + 1][j])
            b.append([l + 1, j])

        if self.num_matrix[l][j - 1] >0 and self.num_matrix[l][j - 1] <998: # left
            a.append(self.num_matrix[l][j - 1])
            b.append([l, j - 1])

        if self.num_matrix[l][j + 1] >0 and self.num_matrix[l][j + 1] < 998: # right
            a.append(self.num_matrix[l][j + 1])
            b.append([l, j + 1])

        if self.num_matrix[l][j]>0 and self.num_matrix[l][j]<998:
            a.append(self.num_matrix[l][j])
            b.append([l, j])

        try:
            path[i] = b[a.index(min(a))]
            l = b[a.index(min(a))][0]
            j = b[a.index(min(a))][1]

        except:
            if self.direction=='up':
                path[1]=[self.y-1, self.x]
            elif self.direction=='down':
                path[1]=[self.y+1, self.x]
            elif self.direction=='right':
                path[1]=[self.y, self.x+1]
            elif self.direction=='left':
                path[1]=[self.y, self.x-1]

            break
    if self!=snake1:
         ## draw matrix
        for i in range(len(self.num_matrix)):
            for j in range(len(self.num_matrix[i])):
                self.screen.move(self.top_corner + i, j * 3)
                if self.num_matrix[i][j] == 0:
                    self.screen.addstr(' 0 ')
                if self.num_matrix[i][j] == 999:
                    self.screen.addstr('99 ')
                elif self.num_matrix[i][j] == 998:
                    self.screen.addstr('98 ')
                else:
                    self.screen.addstr(str(self.num_matrix[i][j])+' ')
    if self!=snake1:
         # draw path
        for i in range(1, len(path)+1):
            self.screen.move(self.top_corner+path[i][0], 5+path[i][1]*3)
            self.screen.addstr('   ', curses.color_pair(2))

        self.screen.addstr(0, 0, str(path)+'                    '*20)

        # draw snakes
        for i in snake1.snakes_list:
            for j in range(1, len(i.snake_body)+1):
                self.screen.move(self.top_corner+i.snake_body[j][1], 5+i.snake_body[j][0]*3)
                self.screen.addstr('  ', curses.color_pair(22))
                self.screen.move(self.top_corner+i.y, 5+i.x*3)
                self.screen.addstr('  ', curses.color_pair(33))

    if self==snake1:
        snake1.screen.addstr(3, 0, str(path)+'                    '*20)

    return path












































































#     ### add new snake
#     def add_snake(self):
#         new_snake=object 
#         new_snake='snake'+str(len(snake1.snakes_list)+1)
#         new_snake = snake()
#         new_snake.second_snake=True
#         new_snake.robot_snake=True
#         new_snake.x=20
#         new_snake.screen=snake1.screen
#         new_snake.initiation()
#         new_snake.screen_dimensions=new_snake.screen.getmaxyx()
#         snake1.snakes_list.append(new_snake)
#     ### delete last snake
#     def delete_snake(self):
#         if len(snake1.snakes_list)>1:
#             snake1.snakes_list.pop(len(snake1.snakes_list)-1)









#     ### tick
#     def tick(self, snake1):         ### двигает змею
#         if self.scene == 'game':

#             if self.robot_snake==True:
#                 self=auto_move_snake(self)
#             if (datetime.datetime.now()-self.timer).microseconds>=100: # 290000
#                 self.timer=datetime.datetime.now()
#                 self=move_head(self)
#                 self, snake1=move_body(self, snake1)

#                 try:
#                     snake1.rotate_keys=snake1.rotate_keys[1:]
#                     snake1.rotate_keys.append(0)
#                 except:
#                     snake1.rotate_keys=[0, 0]


#         if self.scene=='dead':
#             if (datetime.datetime.now()-self.timer).microseconds>=100:
#                 draw_game(self)
#             if (datetime.datetime.now()-self.timer).microseconds>=200: # 580000
#                 self.timer=datetime.datetime.now()
#                 self.deadcount+=1
#             if self.deadcount==5:
#                 self.deadcount=0
#                 self.initiation()

        





# def run_game(screen):
#     curses.curs_set(0)
#     curses.start_color()
#     curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE) # borders
#     curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK) # black
#     curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN) # snake
#     curses.init_pair(3, 0, 10) # head 

#     curses.init_pair(22, 0, 30) # second snake
#     curses.init_pair(33, 0, 50) #second head

#     curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE) # menu 
#     curses.init_pair(16, 15, 9) # game over
#     curses.init_pair(17, curses.COLOR_WHITE, curses.COLOR_GREEN) # lenght
#     curses.init_pair(4, 0, 12*15) # rabbits


#     snake1.screen=screen
#     snake1.screen_dimensions=snake1.screen.getmaxyx()

#     screen.nodelay(True)#, snake1)



#     ############################################# 
#     #
#     #
#     #    main loop 
#     #
#     #
#     #############################################

#     while True:





#             ### GET INPUT
#         getinput(snake1)




#             ### AUTO SNAKE
#         if snake1.scene=='game' and (snake1.robot_snake==True or len(snake1.snakes_list)>1):  ############
#             snake1.wave()



#             ### RABITTS
#         count_rabbits=0

#         for i in range(len(snake1.matrix)):
#             for j in range(len(snake1.matrix[i])):
#                 if snake1.matrix[i][j]==2:
#                     count_rabbits+=1

#         if count_rabbits<1:
#             snake1.rabbit()






        
#         for i in snake1.snakes_list:
#             # if snake1.scene=='game':                                              ###################
#             if snake1.scene=='game':                                              ##################
#                 i.path=i.find_path()
#             draw(i)
#             i.tick(snake1)
#             for i in snake1.snakes_list:

#                 i.path=i.find_path()
#                 draw(i)
#                 i.tick(snake1)

#                 if snake1.scene!='game':
#                     snake1.snakes_list=[snake1]




                
#         for i in snake1.snakes_list: 
#             i.num_matrix=[[ 0 for i in range(40)] for _ in range(40)] 
            
#         snake1.screen.refresh()
        

# snake1 = snake()
# snake1.snakes_list.append(snake1)


# #txt robot snake path
# f = open('robot_snake_path.txt', 'w')
# f.write(' ')
# f.close()


# curses.wrapper(run_game)
















