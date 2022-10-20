import curses

### get input
def getinput(snake1):
    if snake1.second_snake==False:
        key = snake1.screen.getch()
        
        if snake1.scene == 'game':

            if snake1.robot_snake==True:
                if key==ord('a') or key==ord('A'):
                    snake1.screen.clear()
                    snake1.robot_snake=False
            else:
                if key==curses.KEY_LEFT:
                    snake1=rotate_snake(snake1, 'left')
                elif key==curses.KEY_RIGHT:
                    snake1=rotate_snake(snake1, 'right')
                elif key==curses.KEY_DOWN:
                    snake1=rotate_snake(snake1, 'down')
                elif key==curses.KEY_UP:
                    snake1=rotate_snake(snake1, 'up')

                if key==ord('a') or key==ord('A'):
                    snake1.screen.clear()
                    snake1.robot_snake=True

            #####
            if key==ord('l') or key==ord('L'):
                snake1.load_matrix()

            if key==ord('=') or key==ord('+'): #add snake
                snake1.add_snake()
            if key==ord('-') or key==ord('_'): #delete last snake
                snake1.delete_snake()

            if key==ord('p') or key==ord('P'):
                snake1.pause()
                
            elif key==ord('q') or key==ord('Q'):
                snake1.screen.clear()
                snake1.scene='menu'


        elif snake1.scene == 'menu':

            if key==ord('q') or key==ord('Q'):
                pass
            elif key==curses.KEY_UP:
                snake1.menu_item-=1
                if snake1.menu_item==0:
                    snake1.menu_item=3
            elif key==curses.KEY_DOWN:
                snake1.menu_item+=1
                if snake1.menu_item==4:
                    snake1.menu_item=1
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                if snake1.menu_item==3:       # exit
                    sys.exit(0)
                elif snake1.menu_item==1:     # start
                    snake1.screen.clear()
                    snake1.initiation()
                    snake1.scene='game' 
                    snake1.rabbit()
                else:                        # top results
                    snake1.screen.clear()
                    snake1.scene='records'


        elif snake1.scene == 'records':

            if key==curses.KEY_RIGHT:
                snake1.records_item+=1
            elif key==curses.KEY_LEFT:
                snake1.records_item-=1
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                if snake1.records_item==0: # back to menu
                    snake1.screen.clear()
                    snake1.scene='menu'
                elif snake1.records_item==1: # clear records
                    snake1.screen.clear()
                    snake1=clear_records(snake1)

            if snake1.records_item==-1:
                snake1.records_item=1
            elif snake1.records_item==2:
                snake1.records_item=0


        elif snake1.scene == 'save record':
            # запись имени
            if key==curses.KEY_ENTER or key == 10 or key == 13:

                ### добавление рекорда
                add_records(snake1, [snake1.new_name, len(snake1.snake_body)])
                update_file(snake1)

                snake1.screen.clear()
                snake1.screen.refresh()
                snake1.new_name=''
                snake1.scene='records'
            elif key==curses.KEY_BACKSPACE or key==8 or key==127:
                snake1.new_name=snake1.new_name[:-1]
            elif 90<=key<=126:
                if len(snake1.new_name)<10:
                    snake1.new_name+=chr(key)
                        

        elif snake1.scene == 'game over':
            # records
            if len(snake1.records_top)<10:
                snake1.new_name=''
                snake1.scene='save record'
            else:
                for i in range(len(snake1.records_top)):
                    if snake1.records_top[i][1]<len(snake1.snake_body):
                        snake1.new_name=''
                        snake1.scene='save record'

            if key==ord('y') or key==ord('Y'):
                snake1.screen.clear()
                snake1.screen.refresh()
                snake1.__init__()
            elif key==ord('n') or key==ord('N') or key==ord('q') or key==ord('Q'):
                snake1.screen.clear()
                snake1.screen.refresh()
                sys.exit(0)



        if len(snake1.snakes_list)>0:
            for i in snake1.snakes_list:
                if i.scene!='dead':
                    i.scene=snake1.scene

    return snake1



