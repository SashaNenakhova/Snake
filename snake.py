import curses
import datetime
import random


class snake:
    
    ## координаты головы змеи
    x = 15 # left, right
    y = 15 # up, down

    screen = None

    scene = ''
    direction = '' 

    menu_lst=['    SNAKE ', 'Start new game', ' Top results  ', '     Exit     ']
    menu_item=1
    records_lst=[' Back ', ' Clear results ']
    records_item=0
    new_name=''

    robot_snake=False

    ### initiation
    def __init__(self):
        screen = None

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
        self.robot_snake=False
        self.scene='game'
        self.snake_body={i:[self.x, self.y+i-1] for i in range(1, 8)}
        self.delete_rabbits()
        self.rabbit()










    ### has screen changed
    def has_screen_changed(self):

        current_dimensions = self.screen.getmaxyx()

        ## terminal too small
        while self.screen.getmaxyx()[0]<len(self.matrix)+4 or self.screen.getmaxyx()[1]<len(self.matrix[0])*2+3:
            current_dimensions = self.screen.getmaxyx()
            
            ## exit
            key=self.screen.getch()
            if key==ord('q'):
                self.screen.clear()
                exit(0)

            ## screen has changed
            if self.screen_dimensions != current_dimensions:
                self.screen_dimensions = current_dimensions
                self.screen.clear()

            ## terminal too small
            if self.screen.getmaxyx()[0]<len(self.matrix)+4 or self.screen.getmaxyx()[1]<len(self.matrix[0])*2+3:
                self.screen.move(self.screen.getmaxyx()[0]//2, self.screen.getmaxyx()[1]//2-9)
                self.screen.addstr('Terminal too small', curses.color_pair(16))
            elif self.screen.getmaxyx()[0]<3 or self.screen.getmaxyx()[1]<20:
                self.screen.move(self.screen.getmaxyx()[0]//2, self.screen.getmaxyx()[1]//2-3)
                self.screen.addstr('Error', curses.color_pair(16))
            else:
                self.screen.addstr(0, 0, ' ')

        ## screen has changed
        if current_dimensions != self.screen_dimensions:
            self.screen_dimensions = current_dimensions
            self.screen.clear()










    ### draw
    def draw(self):
        ## corners
        self.left_corner = (self.screen.getmaxyx()[1])//2 - len(self.matrix[0])-15 # ширина. (-36)
        self.top_corner = (self.screen.getmaxyx()[0])//2 - len(self.matrix)//2 # высота. (-14)
        self.has_screen_changed()

        ## draw scenes
        if self.scene == 'menu':
            self.draw_menu()
        elif self.scene == 'game':
            self.draw_game()
        elif self.scene == 'game over':
            self.draw_game_over()
        elif self.scene == 'save record':
            pass
        elif self.scene == 'records':
            pass


        self.screen.refresh()

        ## 
        # self.screen.addstr(0, 0, str(self.screen.getmaxyx()[0]) + ' height')
        # self.screen.addstr(1, 0, str(self.screen.getmaxyx()[1]) + ' width')

    ### draw menu
    def draw_menu(self):
        for i in range(4):
            if self.menu_item==i and self.menu_item!=0:
                self.screen.addstr((self.screen.getmaxyx()[0] - 7+i*4) // 2, (self.screen.getmaxyx()[1]-14) // 2, self.menu_lst[i], curses.color_pair(6))
            else:
                self.screen.addstr((self.screen.getmaxyx()[0] - 7+i*4) // 2, (self.screen.getmaxyx()[1]-14) // 2, self.menu_lst[i])

    ### draw game
    def draw_game(self):
        ## draw matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.screen.move(self.top_corner+i, self.left_corner+j*2)
                if self.matrix[i][j]==0:
                    self.screen.addstr('  ', curses.color_pair(10))
                elif self.matrix[i][j]==1:
                    self.screen.addstr('  ', curses.color_pair(1))
                elif self.matrix[i][j]==2:
                    self.screen.addstr('  ', curses.color_pair(4))

        ## draw snake
        for i in range(2, len(self.snake_body)+1):
            self.screen.move(self.top_corner+self.snake_body[i][1], self.left_corner+self.snake_body[i][0]*2)
            self.screen.addstr('  ', curses.color_pair(2))

        ## draw snake head
        for i in range(len(self.snake_head)):
            for j in range(len(self.snake_head[i])):
                self.screen.move(self.top_corner+self.y, self.left_corner+self.x*2)
                self.screen.addstr('  ', curses.color_pair(3))

        ## lenght
        self.screen.addstr(self.top_corner+2, self.left_corner+len(self.matrix)*2+10, 'Lenght', curses.color_pair(5))
        self.screen.addstr(self.top_corner+4, self.left_corner+len(self.matrix)*2+12, str(len(self.snake_body)))

    ### game over
    def draw_game_over(self):
        box1 = curses.newwin(6, 21, self.top_corner+10, self.left_corner+17)
        box1.box()
        box1.bkgd(' ', curses.color_pair(16))    

        box1.addstr(1, 6, 'Game over', curses.color_pair(16))
        box1.addstr(3, 1, 'Type "y" to restart')
        box1.addstr(4, 3, 'or "n" to quit')
        box1.refresh()














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
            self.delete_rabbits()
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
        self.delete_rabbits()

        y, x=random.randint(1, 28), random.randint(1, 28)
        for i in range(1, len(self.snake_body)+1):
            if self.snake_body[i]==[x, y]:
                self.rabbit()
        self.matrix[y][x]=2





    ### pause
    def pause(self):
        self.screen.nodelay(False)

        key=0
        while key!=ord('p'):
            box2 = curses.newwin(3, 10, self.screen.getmaxyx()[0]//2, self.screen.getmaxyx()[1]//2)
            box2.box()
            box2.bkgd(' ', curses.color_pair(16))    
            box2.addstr(1, 2, 'Paused', curses.color_pair(16))
            box2.refresh()
            self.screen.refresh()

            key=self.screen.getch()

            self.draw()

        box2.bkgd(' ', curses.color_pair(0))
        box2.clear()
        box2.refresh()

        self.screen.nodelay(True)

    ### find path
    def find_path(self, screen, matrix, x, y):
        numbered_matrix=[[ 0 for i in range(30)] for _ in range(30)]
        num = 1
        pathfound = False
        end_y, end_x = 0, 0
        rabbit_exist=False

        # set end x, end y, borders
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==1:
                    numbered_matrix[i][j]=999 # border
                elif matrix[i][j]==2: # rabbit
                    end_y, end_x=i, j
                    rabbit_exist=True

        # set snake body
        for i in range(1, len(self.snake_body)+1):
            numbered_matrix[self.snake_body[i][1]][self.snake_body[i][0]]=999

        # set snake head, rabbit
        numbered_matrix[y][x]=1
        numbered_matrix[end_y][end_x]=998



        # num, end_x, end_y >>>> numbered matrix
        while pathfound == False:
            # проходим матрицу и заполняем её значениями дистанции от стартовой точки
            for l in range(len(numbered_matrix)):
                for j in range(len(numbered_matrix[l])):

                    if (numbered_matrix[l][j] == 0 or numbered_matrix[l][j]==998):
                        # надо определить, есть ли в ближайшем окружении заполненные ячейки, и, если есть, выбрать среди них наименьшую

                        found = False
                        value = 999

                        # up
                        if (numbered_matrix[l - 1][j] <= 998) and (numbered_matrix[l - 1][j] > 0):
                            found = True
                            if numbered_matrix[l - 1][j] < value:
                                value = numbered_matrix[l - 1][j]
                        # down
                        if (numbered_matrix[l + 1][j] <= 998) and (numbered_matrix[l + 1][j] > 0):
                            found = True
                            if numbered_matrix[l + 1][j] < value:
                                value = numbered_matrix[l + 1][j]
                        # left
                        if (numbered_matrix[l][j - 1] <= 998) and (numbered_matrix[l][j - 1] > 0):
                            found = True
                            if numbered_matrix[l][j - 1] < value:
                                value = numbered_matrix[l][j - 1]
                        # right
                        if (numbered_matrix[l][j + 1] <= 998) and (numbered_matrix[l][j + 1] > 0):
                            found = True
                            if numbered_matrix[l][j + 1] < value:
                                value = numbered_matrix[l][j + 1]

                        # adding numbers to matrix
                        if (found == True) and (value < num):
                            numbered_matrix[l][j] = value + 1

                        # found rabbit
                        if numbered_matrix[end_y][end_x]==value+1 and found==True:
                            pathfound = True
            num += 1

        # numbered matrix, end x, end y >>>> path
        # path lenght = num
        path, path_j, path_l= {}, end_x, end_y
        for i in range(num-3, 0, -1):

            a = [] # список значений из numbered matrix
            l = [] # список соответствующих им координат
            if numbered_matrix[path_l - 1][path_j] != 0 and numbered_matrix[path_l - 1][path_j] < 999:
                a.append(numbered_matrix[path_l - 1][path_j])
                l.append([path_l - 1, path_j])
            if numbered_matrix[path_l + 1][path_j] != 0 and numbered_matrix[path_l + 1][path_j] < 999:
                a.append(numbered_matrix[path_l + 1][path_j])
                l.append([path_l + 1, path_j])
            if numbered_matrix[path_l][path_j - 1] != 0 and numbered_matrix[path_l][path_j - 1] < 999:
                a.append(numbered_matrix[path_l][path_j - 1])
                l.append([path_l, path_j - 1])
            if numbered_matrix[path_l][path_j + 1] != 0 and numbered_matrix[path_l][path_j + 1] < 999:
                a.append(numbered_matrix[path_l][path_j + 1])
                l.append([path_l, path_j + 1])

            path[i] = l[a.index(min(a))]
            path_l = l[a.index(min(a))][0]
            path_j = l[a.index(min(a))][1]

        if len(path)==0:
            path[1]=[end_y, end_x]

        self.screen.addstr(2, 5, str(path) + '   ' + str(self.x) + '   ' + str(self.y))
        self.screen.addstr(10, 70, str(num) + '   num')
        # for i in range(len(numbered_matrix)):
        #     self.screen.addstr(20+i, 40+i*2, str(numbered_matrix))
        self.screen.refresh()

        ## draw matrix
        for i in range(len(numbered_matrix)):
            for j in range(len(numbered_matrix[i])):
                self.screen.move(5 + i, 5 + j * 2)
                if numbered_matrix[i][j] == 0:
                    self.screen.addstr('  ', curses.color_pair(10))
                elif numbered_matrix[i][j] == 999:
                    self.screen.addstr('  ', curses.color_pair(1))
                elif numbered_matrix[i][j] == 998:
                    self.screen.addstr('  ', curses.color_pair(4))
                else:
                    self.screen.addstr(str(numbered_matrix[i][j])+' ')

        ## draw path
        for i in range(1, len(path)+1):
            self.screen.move(5+path[i][0], 5+path[i][1]*2)
            self.screen.addstr('  ', curses.color_pair(2))
        return path

    ### auto snake
    def auto_move_snake(self):
            path=self.find_path(self.screen, self.matrix, self.x, self.y)

            if path[1][1]<self.x:
                self.rotate_snake('left')
            if path[1][1]>self.x:
                self.rotate_snake('right')
            if path[1][0]<self.y:
                self.rotate_snake('up')
            if path[1][0]>self.y:
                self.rotate_snake('down')



    ### tick
    def tick(self):         ### двигает змею
        if self.scene == 'game':
            if (datetime.datetime.now()-self.timer).microseconds>=290000:
                self.timer=datetime.datetime.now()
                self.move_head()
                self.move_body()


    ### get input
    def getinput(self):
        key = self.screen.getch()
        
        if self.scene == 'game':

            if self.robot_snake==True:
                self.auto_move_snake()
                if key==ord('a'):
                    self.robot_snake=False
            else:
                if key==curses.KEY_LEFT:
                    self.rotate_snake('left')
                elif key==curses.KEY_RIGHT:
                    self.rotate_snake('right')
                elif key==curses.KEY_DOWN:
                    self.rotate_snake('down')
                elif key==curses.KEY_UP:
                    self.rotate_snake('up')

                elif key==ord('a'):
                    self.robot_snake=True

            if key==ord('p'):
                self.pause()
            elif key==ord('q'):
                self.screen.clear()
                self.scene='menu'

        elif self.scene == 'menu':

            if key==curses.KEY_UP:
                self.menu_item-=1
                if self.menu_item==0:
                    self.menu_item=3
            elif key==curses.KEY_DOWN:
                self.menu_item+=1
                if self.menu_item==4:
                    self.menu_item=1
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                if self.menu_item==3:       # exit
                    sys.exit(0)
                elif self.menu_item==1:     # start
                    self.screen.clear()
                    self.initiation()
                    self.scene='game' 
                else:                        # top results
                    self.screen.clear()
                    self.scene='records'

        elif self.scene == 'game over':
            if key==ord('y'):
                self.screen.clear()
                self.screen.refresh()
                self.__init__()
            elif key==ord('n') or key==ord('q'):
                self.screen.clear()
                self.screen.refresh()
                
                sys.exit(0)






def run_game(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE) # borders
    curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK) # black
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN) # snake
    curses.init_pair(5, curses.COLOR_YELLOW, 0) # lenght
    curses.init_pair(3, 0, 10) # head 
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE) # menu 
    curses.init_pair(16, 15, 9) # game over
    curses.init_pair(4, 0, 12*15) # rabbits

    snake.screen=screen
    snake.screen_dimensions=snake.screen.getmaxyx()

    screen.nodelay(True)
    while True:
        snake.getinput()
        snake.draw()
        snake.tick()
        




snake = snake()

curses.wrapper(run_game)








