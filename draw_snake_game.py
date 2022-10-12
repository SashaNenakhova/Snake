import curses



### draw
def draw(snake):
    ## corners
    snake.left_corner = (snake.screen.getmaxyx()[1])//2 - len(snake.matrix[0])-15 # ширина. (-36)
    snake.top_corner = (snake.screen.getmaxyx()[0])//2 - len(snake.matrix)//2 # высота. (-14)
    snake.has_screen_changed()



    ## draw scenes
    if snake.second_snake==True:
        if snake.scene=="game":
            draw_game(snake)

    else:
        ## draw scenes
        if snake.scene == 'menu':
            draw_menu(snake)
        elif snake.scene == 'game':
            draw_game(snake)
        elif snake.scene == 'game over':
            draw_game_over(snake)
        elif snake.scene == 'save record':
            draw_saving_record(snake)
        elif snake.scene == 'records':
            draw_records(snake)
    

    

### draw menu
def draw_menu(snake):
    for i in range(4):
        if snake.menu_item==i and snake.menu_item!=0:
            snake.screen.addstr((snake.screen.getmaxyx()[0] - 7+i*4) // 2, (snake.screen.getmaxyx()[1]-14) // 2, snake.menu_lst[i], curses.color_pair(6))
        else:
            snake.screen.addstr((snake.screen.getmaxyx()[0] - 7+i*4) // 2, (snake.screen.getmaxyx()[1]-14) // 2, snake.menu_lst[i])

### draw game
def draw_game(snake):
    if snake.second_snake==False:
        ## draw matrix
        for i in range(len(snake.matrix)):
            for j in range(len(snake.matrix[i])):
                snake.screen.move(snake.top_corner+i, snake.left_corner+j*2)
                if snake.matrix[i][j]==0:
                    snake.screen.addstr('  ', curses.color_pair(10))
                elif snake.matrix[i][j]==1:
                    snake.screen.addstr('  ', curses.color_pair(1))
                elif snake.matrix[i][j]==2:
                    snake.screen.addstr('  ', curses.color_pair(4))
        ## lenght
        snake.screen.addstr(snake.top_corner+2, snake.left_corner+len(snake.matrix)*2+9, ' Lenght ', curses.color_pair(17))
        snake.screen.addstr(snake.top_corner+4, snake.left_corner+len(snake.matrix)*2+12, str(len(snake.snake_body)))
        ## auto snake
        if snake.robot_snake==True:
            snake.screen.addstr(snake.top_corner+7, snake.left_corner+len(snake.matrix)*2+7, ' Auto snake ', curses.color_pair(16))


        ## draw first snake
        for i in range(2, len(snake.snake_body)+1):
            snake.screen.move(snake.top_corner+snake.snake_body[i][1], snake.left_corner+snake.snake_body[i][0]*2)
            snake.screen.addstr('  ', curses.color_pair(2))
        ## draw first snake head
        for i in range(len(snake.snake_head)):
            for j in range(len(snake.snake_head[i])):
                snake.screen.move(snake.top_corner+snake.y, snake.left_corner+snake.x*2)
                snake.screen.addstr('  ', curses.color_pair(3))

    else:
        # ## draw second snake
        # for i in range(2, len(snake.snake_body)+1):
        #     snake1.screen.move(snake1.top_corner+snake.snake_body[i][1], snake1.left_corner+snake.snake_body[i][0]*2)
        #     snake1.screen.addstr('  ', curses.color_pair(22))
        # ## draw second snake head
        # for i in range(len(snake.snake_head)):
        #     for j in range(len(snake.snake_head[i])):
        #         snake1.screen.move(snake1.top_corner+snake.y, snake1.left_corner+snake.x*2)
        #         snake1.screen.addstr('  ', curses.color_pair(33))

        ## draw second snake
        for i in range(2, len(snake.snake_body)+1):
            snake.screen.move(snake.top_corner+snake.snake_body[i][1], snake.left_corner+snake.snake_body[i][0]*2)
            snake.screen.addstr('  ', curses.color_pair(22))
        ## draw second snake head
        for i in range(len(snake.snake_head)):
            for j in range(len(snake.snake_head[i])):
                snake.screen.move(snake.top_corner+snake.y, snake.left_corner+snake.x*2)
                snake.screen.addstr('  ', curses.color_pair(33))





### game over
def draw_game_over(snake):
    box1 = curses.newwin(6, 21, snake.top_corner+10, snake.left_corner+17)
    box1.box()
    box1.bkgd(' ', curses.color_pair(16))    

    box1.addstr(1, 6, 'Game over', curses.color_pair(16))
    box1.addstr(3, 1, 'Type "y" to restart')
    box1.addstr(4, 3, 'or "n" to quit')
    box1.refresh()









### draw records
def draw_records(snake):
    snake.screen.addstr(snake.screen.getmaxyx()[0]//2-12, snake.screen.getmaxyx()[1]//2-14+8, '  Top records')

    ## draw records list
    for i in range(1, len(snake.records_top)+1):
        j=i-1
        snake.screen.addstr((snake.screen.getmaxyx()[0]) // 2 - 12+2*i, (snake.screen.getmaxyx()[1]) // 2 - 14+2, str(i)+' '+snake.records_top[j][0])
        snake.screen.addstr((snake.screen.getmaxyx()[0]) // 2 - 12+2*i, (snake.screen.getmaxyx()[1]) // 2 - 14+4+len(snake.records_top[j][0])-1+len(str(j)), '-'*((24-len(snake.records_top[j][0])+1-len(str(j)))+3))
        snake.screen.addstr((snake.screen.getmaxyx()[0]) // 2 - 12+2*i, (snake.screen.getmaxyx()[1]) // 2 - 14+4+24+3-len(str(snake.records_top[j][1])), str(snake.records_top[j][1]))
   
    ## draw back, clear records
    for i in range(2):
        if snake.records_item==i:
            # выбранная кнопка
            snake.screen.addstr(snake.screen.getmaxyx()[0]//2-12+2+len(snake.records_top)*2, snake.screen.getmaxyx()[1]//2-14+18*i, snake.records_lst[i], curses.color_pair(6))
        else:
            snake.screen.addstr(snake.screen.getmaxyx()[0]//2-12+2+len(snake.records_top)*2, snake.screen.getmaxyx()[1]//2-14+18*i, snake.records_lst[i])


### draw saving record
def draw_saving_record(snake):
    box2 = curses.newwin(5, 35, snake.top_corner+18, snake.left_corner+21)
    box2.box()
    box2.bkgd(' ', curses.color_pair(16))    
    box2.addstr(1, 1, 'You have achieved the high score!', curses.color_pair(16))
    box2.addstr(3, 1, 'Please, type your name:'+snake.new_name, curses.color_pair(16))
    snake.screen.move(snake.top_corner+18, snake.left_corner+44)
    box2.refresh()












