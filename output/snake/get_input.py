import curses
from move_snake import *
from records_functions import *

### get input
def getinput(snake):
    if snake.second_snake==False:
        key = snake.screen.getch()
        
        if snake.scene == 'game':

            if snake.robot_snake==True:
                if key==ord('a') or key==ord('A'):
                    snake.screen.clear()
                    snake.robot_snake=False
            else:

                if snake.rotate_keys.count(0)<2:
                    if key==curses.KEY_LEFT:
                        snake.rotate_keys[1]='left'
                    elif key==curses.KEY_RIGHT:
                        snake.rotate_keys[1]='right'
                    elif key==curses.KEY_DOWN:
                       snake.rotate_keys[1]='down'
                    elif key==curses.KEY_UP:
                        snake.rotate_keys[1]='up'
                else:
                    if key==curses.KEY_LEFT:
                        snake.rotate_keys[0]='left'
                    elif key==curses.KEY_RIGHT:
                        snake.rotate_keys[0]='right'
                    elif key==curses.KEY_DOWN:
                       snake.rotate_keys[0]='down'
                    elif key==curses.KEY_UP:
                        snake.rotate_keys[0]='up'


                try:
                    snake=rotate_snake(snake, snake.rotate_keys[0])
                except:
                    pass

                if key==ord('a') or key==ord('A'):
                    snake.screen.clear()
                    snake.robot_snake=True

            if key==ord('c'): # statistic
                    snake.counting=True

            
            if key==ord('l') or key==ord('L'): # загрузить стакан
                snake.load_matrix()

            if key==ord('=') or key==ord('+'): # add snake
                snake.add_snake()
            if key==ord('-') or key==ord('_'): # delete last snake
                snake.delete_snake()

            if key==ord('p') or key==ord('P'): # pause
                snake.pause()
                
            elif key==ord('q') or key==ord('Q'): # exit
                snake.screen.clear()
                snake.scene='menu'


        elif snake.scene == 'menu':

            if key==ord('q') or key==ord('Q'):
                pass
            elif key==curses.KEY_UP:
                snake.menu_item-=1
                if snake.menu_item==0:
                    snake.menu_item=3
            elif key==curses.KEY_DOWN:
                snake.menu_item+=1
                if snake.menu_item==4:
                    snake.menu_item=1
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                if snake.menu_item==3:       # exit
                    sys.exit(0)
                elif snake.menu_item==1:     # start
                    snake.screen.clear()
                    snake.initiation()
                    snake.scene='game' 
                    snake.rabbit()
                else:                        # top results
                    snake.screen.clear()
                    snake.scene='records'


        elif snake.scene == 'records':

            if key==curses.KEY_RIGHT:
                snake.records_item+=1
            elif key==curses.KEY_LEFT:
                snake.records_item-=1
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                if snake.records_item==0: # back to menu
                    snake.screen.clear()
                    snake.scene='menu'
                elif snake.records_item==1: # clear records
                    snake.screen.clear()
                    snake=clear_records(snake)

            if snake.records_item==-1:
                snake.records_item=1
            elif snake.records_item==2:
                snake.records_item=0


        elif snake.scene == 'save record':
            # запись имени
            if key==curses.KEY_ENTER or key == 10 or key == 13:

                ### добавление рекорда
                add_records(snake, [snake.new_name, len(snake.snake_body)])
                update_file(snake)

                snake.screen.clear()
                snake.screen.refresh()
                snake.new_name=''
                snake.scene='records'
            elif key==curses.KEY_BACKSPACE or key==8 or key==127:
                snake.new_name=snake.new_name[:-1]
            elif 90<=key<=126:
                if len(snake.new_name)<10:
                    snake.new_name+=chr(key)
                        

        elif snake.scene == 'game over':


            # records
            if len(snake.records_top)<10:
                snake.new_name=''
                snake.scene='save record'
            else:
                for i in range(len(snake.records_top)):
                    if snake.records_top[i][1]<len(snake.snake_body):
                        snake.new_name=''
                        snake.scene='save record'

            if key==ord('y') or key==ord('Y'):
                snake.screen.clear()
                snake.screen.refresh()
                snake.__init__()
            elif key==ord('n') or key==ord('N') or key==ord('q') or key==ord('Q'):
                snake.screen.clear()
                snake.screen.refresh()
                sys.exit(0)



        if len(snake.snakes_list)>0:
            for i in snake.snakes_list:
                if i.scene!='dead':
                    i.scene=snake.scene



