import curses
import datetime


class snake:
    
    ## координаты головы змеи
    x = 15 # left, right
    y = 15 # up, down

    screen = None

    scene = ''
    direction = '' 

    menu_lst=['    SNAKE ', 'Start new game', ' Top results  ', '     Exit     ']
    menu_item=1

    ### initiation
    def __init__(self):
        screen = None

        ## create matrix and a snake
        self.matrix = [[ 0 for i in range(30)] for _ in range(30)]
        self.snake_head = [[0]]
        self.snake_body={i:[self.x, self.y+i-1] for i in range(1, 5)}

        self.color=2

        ## add borders
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i==0 or i==len(self.matrix)-1 or j==0 or j==len(self.matrix[i])-1:
                    self.matrix[i][j]=1

        self.direction = 'up'
        self.scene='menu'
        self.timer = datetime.datetime.now()

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
        self.left_corner = (self.screen.getmaxyx()[1])//2 - len(self.matrix[0])+1 # ширина. (-36)
        self.top_corner = (self.screen.getmaxyx()[0])//2 - len(self.matrix)//2 # высота. (-14)
        self.has_screen_changed()

        ## draw scenes
        if self.scene == 'menu':
            self.draw_menu()
        elif self.scene == 'game':
            self.draw_game()
        elif self.scene == 'game over':
            self.draw_game_over()


        self.screen.refresh()

        ## 
        self.screen.addstr(0, 0, str(self.screen.getmaxyx()[0]) + ' height')
        self.screen.addstr(1, 0, str(self.screen.getmaxyx()[1]) + ' width')
        self.screen.addstr(0, 17, str(self.y) + ' y')
        self.screen.addstr(1, 17, str(self.x) + ' x')
        self.screen.addstr(0, 25, self.direction)
        self.screen.addstr(1, 25, str(self.snake_body))


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

        ## draw snake
        for i in range(2, len(self.snake_body)+1):
            self.screen.move(self.top_corner+self.snake_body[i][1], self.left_corner+self.snake_body[i][0]*2)
            self.screen.addstr('  ', curses.color_pair(2))

        ## draw snake head
        for i in range(len(self.snake_head)):
            for j in range(len(self.snake_head[i])):
                self.screen.move(self.top_corner+self.y, self.left_corner+self.x*2)
                self.screen.addstr('  ', curses.color_pair(3))

    ### game over
    def draw_game_over(self):
        # box1 = curses.newwin(6, 21, self.top_corner+10, self.left_corner+28)
        # box1.box()
        # box1.bkgd(' ', curses.color_pair(16))    

        # box1.addstr(1, 6, 'Game over', curses.color_pair(16))
        # box1.addstr(3, 1, 'Type "y" to restart')
        # box1.addstr(4, 3, 'or "n" to quit')
        # box1.refresh()
        pass

    ### rotate snake
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


    ### move snake
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

    ### move body
    def move_body(self):
        for i in range(len(self.snake_body), 1, -1):
            self.snake_body[i]=self.snake_body[i-1]
        self.snake_body[1]=[self.x, self.y]

    ### can move
    def __can_move(self, new_x, new_y): 
        if self.matrix[new_y][new_x]==0:
            return True
        else:
            return False

    ### tick
    def tick(self):         ### двигает змею
        if self.scene == 'game':
            if (datetime.datetime.now()-self.timer).microseconds>=400000:
                self.timer=datetime.datetime.now()
                self.move_head()
                self.move_body()



    ### get input
    def getinput(self):
        key = self.screen.getch()
        
        if self.scene == 'game':

            if key==curses.KEY_LEFT:
                self.rotate_snake('left')
            elif key==curses.KEY_RIGHT:
                self.rotate_snake('right')
            elif key==curses.KEY_DOWN:
                self.rotate_snake('down')
            elif key==curses.KEY_UP:
                self.rotate_snake('up')
            elif key==ord('p'):
                # self.pause()
                pass
            elif key==ord('q'):
                self.screen.clear()
                self.scene='menu'

        elif self.scene == 'menu':

            if key==ord('q'):
                pass
            elif key==curses.KEY_UP:
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
                    # self.initiation()
                    self.scene='game' 
                else:                        # top results
                    self.screen.clear()
                    self.scene='records'

            elif self.scene == 'game over':
                pass






def run_game(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE) # borders
    curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK) # black
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN) # snake
    curses.init_pair(3, 29, 29) # head
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE) # menu 

    snake.screen=screen
    snake.screen_dimensions=snake.screen.getmaxyx()

    screen.nodelay(True)
    while True:
        snake.getinput()
        snake.draw()
        snake.tick()
        




snake = snake()

curses.wrapper(run_game)








