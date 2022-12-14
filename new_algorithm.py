import curses
import datetime
import random



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

#     snakes_list=[]
#     robot_snake=False
#     second_snake=False
#     deadcount=0

#     ### initiation
#     def __init__(self):
#         screen = None

#         ## create matrix and a snake
#         self.matrix = [[ 0 for i in range(30)] for _ in range(30)]

#         self.snake_head = [[0]]

#         if self.second_snake==True:
#             self.x=20
#             self.snake_body={i:[self.x, self.y] for i in range(1, 8)}
#         else:
        
#             self.snake_body={i:[self.x, self.y+i-1] for i in range(1, 8)}
#             self.scene='menu'
#             self.records_top=self.read_file()



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
#             self.delete_rabbits()
#             self.robot_snake=False
#             self.snake_body={i:[self.x, self.y+i-1] for i in range(1, 8)}

#             self.snakes_list=[snake1]
#             self.num=0

#         self.num_matrix= [[ 0 for i in range(30)] for _ in range(30)]
       

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




#     ### draw
#     def draw(self):
#         ## corners
#         self.left_corner = (self.screen.getmaxyx()[1])//2 - len(self.matrix[0])-15 # ширина. (-36)
#         self.top_corner = (self.screen.getmaxyx()[0])//2 - len(self.matrix)//2 # высота. (-14)
#         self.has_screen_changed()



#         ## draw scenes
#         if self.second_snake==True:
#             if self.scene=="game":
#                 self.draw_game()

#         else:
#             ## draw scenes
#             if self.scene == 'menu':
#                 self.draw_menu()
#             elif self.scene == 'game':
#                 self.draw_game()
#             elif self.scene == 'game over':
#                 self.draw_game_over()
#             elif self.scene == 'save record':
#                 self.draw_saving_record()
#             elif self.scene == 'records':
#                 self.draw_records()
        

        

#     ### draw menu
#     def draw_menu(self):
#         for i in range(4):
#             if self.menu_item==i and self.menu_item!=0:
#                 self.screen.addstr((self.screen.getmaxyx()[0] - 7+i*4) // 2, (self.screen.getmaxyx()[1]-14) // 2, self.menu_lst[i], curses.color_pair(6))
#             else:
#                 self.screen.addstr((self.screen.getmaxyx()[0] - 7+i*4) // 2, (self.screen.getmaxyx()[1]-14) // 2, self.menu_lst[i])

#     ### draw game
#     def draw_game(self):
#         if self.second_snake==False:
#             ## draw matrix
#             for i in range(len(self.matrix)):
#                 for j in range(len(self.matrix[i])):
#                     self.screen.move(self.top_corner+i, self.left_corner+j*2)
#                     if self.matrix[i][j]==0:
#                         self.screen.addstr('  ', curses.color_pair(10))
#                     elif self.matrix[i][j]==1:
#                         self.screen.addstr('  ', curses.color_pair(1))
#                     elif self.matrix[i][j]==2:
#                         self.screen.addstr('  ', curses.color_pair(4))
#             ## lenght
#             self.screen.addstr(self.top_corner+2, self.left_corner+len(self.matrix)*2+9, ' Lenght ', curses.color_pair(17))
#             self.screen.addstr(self.top_corner+4, self.left_corner+len(self.matrix)*2+12, str(len(self.snake_body)))
#             ## auto snake
#             if self.robot_snake==True:
#                 self.screen.addstr(self.top_corner+7, self.left_corner+len(self.matrix)*2+7, ' Auto snake ', curses.color_pair(16))


#             ## draw first snake
#             for i in range(2, len(self.snake_body)+1):
#                 self.screen.move(self.top_corner+self.snake_body[i][1], self.left_corner+self.snake_body[i][0]*2)
#                 self.screen.addstr('  ', curses.color_pair(2))
#             ## draw first snake head
#             for i in range(len(self.snake_head)):
#                 for j in range(len(self.snake_head[i])):
#                     self.screen.move(self.top_corner+self.y, self.left_corner+self.x*2)
#                     self.screen.addstr('  ', curses.color_pair(3))

#         else:
#             ## draw second snake
#             for i in range(2, len(self.snake_body)+1):
#                 snake1.screen.move(snake1.top_corner+self.snake_body[i][1], snake1.left_corner+self.snake_body[i][0]*2)
#                 snake1.screen.addstr('  ', curses.color_pair(22))
#             ## draw second snake head
#             for i in range(len(self.snake_head)):
#                 for j in range(len(self.snake_head[i])):
#                     snake1.screen.move(snake1.top_corner+self.y, snake1.left_corner+self.x*2)
#                     snake1.screen.addstr('  ', curses.color_pair(33))





#     ### game over
#     def draw_game_over(self):
#         box1 = curses.newwin(6, 21, self.top_corner+10, self.left_corner+17)
#         box1.box()
#         box1.bkgd(' ', curses.color_pair(16))    

#         box1.addstr(1, 6, 'Game over', curses.color_pair(16))
#         box1.addstr(3, 1, 'Type "y" to restart')
#         box1.addstr(4, 3, 'or "n" to quit')
#         box1.refresh()









#  ### draw records
#     def draw_records(self):
#         self.screen.addstr(self.screen.getmaxyx()[0]//2-12, self.screen.getmaxyx()[1]//2-14+8, '  Top records')

#         ## draw records list
#         for i in range(1, len(self.records_top)+1):
#             j=i-1
#             self.screen.addstr((self.screen.getmaxyx()[0]) // 2 - 12+2*i, (self.screen.getmaxyx()[1]) // 2 - 14+2, str(i)+' '+self.records_top[j][0])
#             self.screen.addstr((self.screen.getmaxyx()[0]) // 2 - 12+2*i, (self.screen.getmaxyx()[1]) // 2 - 14+4+len(self.records_top[j][0])-1+len(str(j)), '-'*((24-len(self.records_top[j][0])+1-len(str(j)))+3))
#             self.screen.addstr((self.screen.getmaxyx()[0]) // 2 - 12+2*i, (self.screen.getmaxyx()[1]) // 2 - 14+4+24+3-len(str(self.records_top[j][1])), str(self.records_top[j][1]))
       
#         ## draw back, clear records
#         for i in range(2):
#             if self.records_item==i:
#                 # выбранная кнопка
#                 self.screen.addstr(self.screen.getmaxyx()[0]//2-12+2+len(self.records_top)*2, self.screen.getmaxyx()[1]//2-14+18*i, self.records_lst[i], curses.color_pair(6))
#             else:
#                 self.screen.addstr(self.screen.getmaxyx()[0]//2-12+2+len(self.records_top)*2, self.screen.getmaxyx()[1]//2-14+18*i, self.records_lst[i])


#  ### draw saving record
#     def draw_saving_record(self):
#         box2 = curses.newwin(5, 35, self.top_corner+18, self.left_corner+21)
#         box2.box()
#         box2.bkgd(' ', curses.color_pair(16))    
#         box2.addstr(1, 1, 'You have achieved the high score!', curses.color_pair(16))
#         box2.addstr(3, 1, 'Please, type your name:'+self.new_name, curses.color_pair(16))
#         self.screen.move(self.top_corner+18, self.left_corner+44)
#         box2.refresh()













#     ### changes direction of snake head
#     def rotate_snake(self, command):     ### изменяет направление змеи
#         new_x, new_y=self.x, self.y

#         if command=='left' and self.direction!='right':
#             if self.__can_move(new_x-1, new_y) == True:
#                 self.direction='left'

#         elif command=='right' and self.direction!='left':
#             if self.__can_move(new_x+1, new_y) == True:
#                 self.direction='right'

#         elif command=='down' and self.direction!='up':
#             if self.__can_move(new_x, new_y+1) == True:
#                 self.direction='down'

#         elif command=='up' and self.direction!='down':
#             if self.__can_move(new_x, new_y-1) == True:
#                 self.direction='up'

#     ### changes x and y of snake head
#     def move_head(self):
#         if self.direction=='left':
#             if self.__can_move(self.x-1, self.y):
#                 self.x-=1
#         elif self.direction=='right':
#             if self.__can_move(self.x+1, self.y):
#              self.x+=1
#         elif self.direction=='down':
#             if self.__can_move(self.x, self.y+1):
#              self.y+=1
#         elif self.direction=='up':
#             if self.__can_move(self.x, self.y-1):
#                 self.y-=1   

#     ### move body//game over if head doesn't move//snake grow if eat rabbits
#     def move_body(self):
#         # кролик
#         if self.matrix[self.y][self.x]==2:
#             self.snake_body[len(self.snake_body)+1]=self.snake_body[len(self.snake_body)]
#             snake1.rabbit()

#         # движение
#         for i in range(len(self.snake_body), 1, -1):
#             self.snake_body[i]=self.snake_body[i-1] 

#         # врезается в себя
#         for i in range(2, len(self.snake_body)+1):
#             if self.snake_body[i]==[self.x, self.y]: 
#                 if self.second_snake==False:
#                     # self.scene='game over'
#                     pass
#                     self.scene='game over'
                    
#                 else:
#                     self.scene='dead'
#             self.snake_body[1]=[self.x, self.y]

#         # врезается в другую змею
#         if self.second_snake==False:
#             if len(self.snakes_list)>1:
#                 for i in self.snakes_list:
#                     if i!=self:
#                         for j in range(1, len(i.snake_body)+1):
#                             if i.snake_body[j]==[self.x, self.y]: 
#                                 # self.scene='game over'
#                                 pass
#                                 self.scene='game over'

#         else:
#             if len(snake1.snakes_list)>2:
#                 for i in snake1.snakes_list:
#                     if i!=self:
#                         for j in range(1, len(i.snake_body)+1):
#                             if i.snake_body[j]==[self.x, self.y]: 
#                                 self.scene='dead'

#             for j in range(1, len(snake1.snake_body)+1):
#                 if snake1.snake_body[j]==[self.x, self.y]: 
#                     self.scene='dead'



#     ### can move if 0 or rabbit//cant move back
#     def __can_move(self, new_x, new_y): 
#         if self.matrix[new_y][new_x]==0 or self.matrix[new_y][new_x]==2:
#             if self.snake_body[2]==[new_x, new_y]:
#                 return False
#             return True
#         else:
#             return False









#     ### delete rabbits
#     def delete_rabbits(self):
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[i])):
#                 if self.matrix[i][j]==2:
#                     self.matrix[i][j]=0

#     ### generate rabbits
#     def rabbit(self):
#         if self.second_snake==False:
#             self.delete_rabbits()

#             y, x=random.randint(1, 28), random.randint(1, 28)

#             if self.matrix[y][x]==1:
#                 self.rabbit()
#             else:
#                 self.matrix[y][x]=2

#             for i in range(1, len(self.snake_body)+1):
#                 if self.snake_body[i]==[x, y]:
#                     self.delete_rabbits()
#                     self.rabbit()

#             if len(self.snakes_list)>1:
#                 for i in self.snakes_list:
#                     for j in range(1, len(i.snake_body)+1):
#                         if i.snake_body[j]==[x, y]:
#                             self.delete_rabbits()
#                             self.rabbit()
        

#         else:
#             self.delete_rabbits()

#             for i in range(1, len(self.snake_body)+1):     
#                 if self.snake_body[i]==[x, y]:
#                     self.delete_rabbits()
#                     self.rabbit()

#             for i in range(len(snake1.matrix)):
#                 for j in range(len(snake1.matrix[i])):
#                     if snake1.matrix[i][j]==2:
#                         self.matrix[y][x]=2





#  ### pause
#     def pause(self):
#         self.screen.nodelay(False)

#         key=0
#         while key!=ord('p'):
#             box = curses.newwin(3, 10, self.screen.getmaxyx()[0]//2, self.screen.getmaxyx()[1]//2)
#             box.box()
#             box.bkgd(' ', curses.color_pair(16))    
#             box.addstr(1, 2, 'Paused', curses.color_pair(16))
#             box.refresh()

#             key=self.screen.getch()

#             self.draw()

#         box.bkgd(' ', curses.color_pair(0))
#         box.clear()
#         box.refresh()

#         self.screen.nodelay(True)













































# find path
def find_path2(self, matrix): # -screen, self
    self.num_matrix = [[ 0 for i in range(30)] for _ in range(30)]

    # rabbit
    for l in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[l][j]==2:
                snake1.num_matrix[l][j]=1
                # end_x=j
                # end_y=l

    # snake body
    steps=0
    a1, b1=0, 0
    snake_body=0 
    for i in snake1.snakes_list:
        snake_body=i.snake_body
        self.num_matrix[i.y][i.x]=999   
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






        # snake head
        self.num_matrix[self.y][self.x]=998
        end_x=self.x
        end_y=self.y

    if self==snake1:

        # borders
        for l in range(len(matrix)):
            for j in range(len(matrix[l])):
                if matrix[l][j]==1:
                    snake1.num_matrix[l][j]=999


        # # snake head
        # snake1.num_matrix[self.y][self.x]=998

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
                            if snake1.num_matrix[l-1][j]<value and snake1.num_matrix[l-1][j]!=0: # поиск наименьшего значения 
                                value = snake1.num_matrix[l-1][j]

                        # нижняя клетка
                        if snake1.num_matrix[l+1][j]<998 and snake1.num_matrix[l+1][j]>0: 
                            found=True
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


                        # проверить если путь найден
                        # if end_y==l and end_x==j and found==True:
                        if snake1.num>50:
                            pathfound=True


                        # увеличить значение в центральной клетке до наименьшего+1
                        # if found==True and value<snake1.num and snake1.num_matrix[l][j]==0:
                        if found==True and snake1.num_matrix[l][j]==0:
                            snake1.num_matrix[l][j]=value+1

            snake1.num+=1
            if snake1.num>100:
                pathnotfound=True
                pathfound=True




        # на пути хвост
        if pathnotfound==True:
            # поиск пути к наибольшему значению (самой дальней клетке)
            max_num=0
            for i in range(len(snake1.num_matrix)):
                for j in range(len(snake1.num_matrix[i])):
                    if snake1.num_matrix[i][j]>max_num and snake1.num_matrix[i][j]<998:
                        max_num=snake1.num_matrix[i][j]
                        end_y=i
                        end_x=j



    ### second snakes matrix (snakes bodies + snake1.num_matrix)
    if self!=snake1:
        for i in range(len(self.num_matrix)):
            for j in range(len(self.num_matrix)):
                if self.num_matrix[i][j]!=999:
                    self.num_matrix[i][j]=snake1.num_matrix[i][j]




    # numbered matrix, end x, end y >>>> path
    # path lenght = num
    path, j, l= {}, end_x, end_y


    # for i in range(snake1.num-2, 0, -1):
    for i in range(1, snake1.num-1):

        a = [] # список значений из numbered matrix
        b = [] # список соответствующих им координат


        if self.num_matrix[l - 1][j] >0 and self.num_matrix[l - 1][j] < 998: # up
            a.append(self.num_matrix[l - 1][j])
            b.append([l - 1, j])

        if self.num_matrix[l + 1][j] >0 and self.num_matrix[l + 1][j] < 998: # down

            a.append(self.num_matrix[l + 1][j])
            b.append([l + 1, j])

        if self.num_matrix[l][j - 1] >0 and self.num_matrix[l][j - 1] < 998: # left
            a.append(self.num_matrix[l][j - 1])
            b.append([l, j - 1])

        if self.num_matrix[l][j + 1] >0 and self.num_matrix[l][j + 1] < 998: # right
            a.append(self.num_matrix[l][j + 1])
            b.append([l, j + 1])

        if self.num_matrix[l][j]>0 and self.num_matrix[l][j]<998:
            a.append(self.num_matrix[l][j])
            b.append([l, j])

        if len(a)==0:
            path[1]=[end_y, end_x]
        else:
            path[i] = b[a.index(min(a))]
            l = b[a.index(min(a))][0]
            j = b[a.index(min(a))][1]  
    # if len(path)==0:
    #     path[1]=[end_y, end_x]










    if self==snake1:
        ## draw matrix
        for i in range(len(self.num_matrix)):
            for j in range(len(self.num_matrix[i])):
                self.screen.move(5 + i, 5 + j * 2)
                if self.num_matrix[i][j] == 0:
                    self.screen.addstr(' 0')
                if self.num_matrix[i][j] == 999:
                    self.screen.addstr('99')
                elif self.num_matrix[i][j] == 998:
                    self.screen.addstr('98')
                else:
                    self.screen.addstr(str(self.num_matrix[i][j])+' ')
        # draw path
        for i in range(1, len(path)+1):
            self.screen.move(5+path[i][0], 5+path[i][1]*2)
            self.screen.addstr('  ', curses.color_pair(2))

        self.screen.addstr(0, 0, str(pathfound)+' '+str(snake1.num)+'  '+str(pathnotfound) + ' '+str(path)+'                    '*20)

  

    return path
















































#     ### auto snake
#     def auto_move_snake(self):
#         path=self.find_path(self.matrix) 
#         if path[1][1]<self.x:
#             if self.direction!='right':
#                 self.rotate_snake('left')
#             else:
#                 self.rotate_snake('down')
#         elif path[1][1]>self.x:
#             if self.direction!='left':
#                 self.rotate_snake('right')
#             else:
#                 self.rotate_snake('up')
#         elif path[1][0]<self.y:
#             if self.direction!='down':
#                 self.rotate_snake('up')
#             else:
#                 self.rotate_snake('left')
#         elif path[1][0]>self.y:
#             if self.direction!='up':
#                 self.rotate_snake('down')
#             else:
#                 self.rotate_snake('right')






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
#     def tick(self):         ### двигает змею
#         if self.scene == 'game':
#             if self.robot_snake==True:
#                 self.auto_move_snake()
#             # if (datetime.datetime.now()-self.timer).microseconds>=100000: ####### 290000
#             if (datetime.datetime.now()-self.timer).microseconds>=290000: ####### 290000
#                 self.timer=datetime.datetime.now()
#                 self.move_head()
#                 self.move_body()

#         if self.scene=='dead':
#             # if (datetime.datetime.now()-self.timer).microseconds>=100000:
#             if (datetime.datetime.now()-self.timer).microseconds>=290000:
#                 self.draw_game()
#             # if (datetime.datetime.now()-self.timer).microseconds>=200000: ######## 580000
#             if (datetime.datetime.now()-self.timer).microseconds>=580000: ######## 580000
#                 self.timer=datetime.datetime.now()
#                 self.deadcount+=1
#             if self.deadcount==5:
#                 self.deadcount=0
#                 self.initiation()

            



#     ### get input
#     def getinput(self):
#         if self.second_snake==False:
#             key = self.screen.getch()
            
#             if self.scene == 'game':

#                 if self.robot_snake==True:
#                     if key==ord('a'):
#                         self.screen.clear()
#                         self.robot_snake=False
#                 else:
#                     if key==curses.KEY_LEFT:
#                         self.rotate_snake('left')
#                     elif key==curses.KEY_RIGHT:
#                         self.rotate_snake('right')
#                     elif key==curses.KEY_DOWN:
#                         self.rotate_snake('down')
#                     elif key==curses.KEY_UP:
#                         self.rotate_snake('up')

#                     if key==ord('a'):
#                         self.screen.clear()
#                         self.robot_snake=True

#                 if key==ord('='): #add snake
#                     self.add_snake()
#                 if key==ord('-'): #delete last snake
#                     self.delete_snake()

#                 if key==ord('p'):
#                     self.pause()
                    
#                 elif key==ord('q'):
#                     self.screen.clear()
#                     self.scene='menu'


#             elif self.scene == 'menu':

#                 if key==ord('q'):
#                     pass
#                 elif key==curses.KEY_UP:
#                     self.menu_item-=1
#                     if self.menu_item==0:
#                         self.menu_item=3
#                 elif key==curses.KEY_DOWN:
#                     self.menu_item+=1
#                     if self.menu_item==4:
#                         self.menu_item=1
#                 elif key == curses.KEY_ENTER or key == 10 or key == 13:
#                     if self.menu_item==3:       # exit
#                         sys.exit(0)
#                     elif self.menu_item==1:     # start
#                         self.screen.clear()
#                         self.initiation()
#                         self.scene='game' 
#                         self.rabbit()
#                     else:                        # top results
#                         self.screen.clear()
#                         self.scene='records'


#             elif self.scene == 'records':

#                 if key==curses.KEY_RIGHT:
#                     self.records_item+=1
#                 elif key==curses.KEY_LEFT:
#                     self.records_item-=1
#                 elif key == curses.KEY_ENTER or key == 10 or key == 13:
#                     if self.records_item==0: # back to menu
#                         self.screen.clear()
#                         self.scene='menu'
#                     elif self.records_item==1: # clear records
#                         self.screen.clear()
#                         self.clear_records()

#                 if self.records_item==-1:
#                     self.records_item=1
#                 elif self.records_item==2:
#                     self.records_item=0


#             elif self.scene == 'save record':
#                 # запись имени
#                 if key==curses.KEY_ENTER or key == 10 or key == 13:

#                     ### добавление рекорда
#                     self.add_records([self.new_name, len(self.snake_body)])
#                     self.update_file()

#                     self.screen.clear()
#                     self.screen.refresh()
#                     self.new_name=''
#                     self.scene='records'
#                 elif key==curses.KEY_BACKSPACE or key==8 or key==127:
#                     self.new_name=self.new_name[:-1]
#                 elif 90<=key<=126:
#                     if len(self.new_name)<10:
#                         self.new_name+=chr(key)
                            

#             elif self.scene == 'game over':
#                 # records
#                 if len(self.records_top)<10:
#                     self.new_name=''
#                     self.scene='save record'
#                 else:
#                     for i in range(len(self.records_top)):
#                         if self.records_top[i][1]<len(self.snake_body):
#                             self.new_name=''
#                             self.scene='save record'

#                 if key==ord('y'):
#                     self.screen.clear()
#                     self.screen.refresh()
#                     self.__init__()
#                 elif key==ord('n') or key==ord('q'):
#                     self.screen.clear()
#                     self.screen.refresh()
#                     sys.exit(0)



#             if len(self.snakes_list)>0:
#                 for i in self.snakes_list:
#                     if i.scene!='dead':
#                         i.scene=snake1.scene




















# ########### RECORDS ###########

#     ### updating file
#     def update_file(self):
#         file = open('records.txt', 'w')
#         strings = []
#         # списки из records_top формируются в список строк
#         for i in self.records_top: 
#             if len(i)==2:
#                 strings.append(i[0] + ';' + str(i[1]))
#         # строки добавляются в конец файла
#         for i in strings: 
#             file.write(i+'\n')
#         file.close()

#     ### copy file to records_top
#     def read_file(self):
#         read=[]
#         try:
#             file=open('records.txt')
#             str_list=file.read().split('\n')
#             for i in str_list:
#                 if ';' in i:
#                     spl=i.split(';')
#                     read.append([spl[0], int(spl[1])])
#         except FileNotFoundError:
#             file = open('records.txt', 'w')
#             file.write('')
#         file.close()
#         return read

#     ### add record to records_top
#     def add_records(self, record):
#         if self.records_top==[]:   # если список пустой
#             self.records_top.append(record)
#         else:
#             for i in range(len(self.records_top)):
#                 if self.records_top[i][1]<record[1]:  # если есть рекорд меньше
#                     self.records_top.insert(i, record)
#                     break
#             else:
#                 if len(self.records_top)<10:  # если нет рекордов меньше но есть место в списке
#                     self.records_top.append(record)

#         if len(self.records_top)==11:   # удаление лишних строк
#             self.records_top=self.records_top[:-1]

#     ### clear records
#     def clear_records(self):
#         file=open('records.txt', 'w')
#         file.write('')
#         file.close()
#         self.records_top=[]

























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

#     screen.nodelay(True)
#     while True:

#         for i in snake1.snakes_list:
#             i.matrix=snake1.matrix
#             i.getinput()
#             i.draw()
#             i.tick()
#         snake1.screen.refresh()
        


# snake1 = snake()
# snake1.snakes_list.append(snake1)


# #txt robot snake2 path
# f = open('robot_snake_path.txt', 'w')
# f.write(' ')
# f.close()


# curses.wrapper(run_game)
