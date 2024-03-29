
### changes direction of snake head
def rotate_snake(snake, command):     ### изменяет направление змеи
    new_x, new_y=snake.x, snake.y

    if command=='left' and snake.direction!='right':
        if __can_move(snake, new_x-1, new_y) == True:
            snake.direction='left'

    elif command=='right' and snake.direction!='left':
        if __can_move(snake, new_x+1, new_y) == True:
            snake.direction='right'

    elif command=='down' and snake.direction!='up':
        if __can_move(snake, new_x, new_y+1) == True:
            snake.direction='down'

    elif command=='up' and snake.direction!='down':
        if __can_move(snake, new_x, new_y-1) == True:
            snake.direction='up'

    return snake




### changes x and y of snake head
def move_head(snake):
    if snake.direction=='left':
        if __can_move(snake, snake.x-1, snake.y):
            snake.x-=1
    elif snake.direction=='right':
        if __can_move(snake, snake.x+1, snake.y):
         snake.x+=1
    elif snake.direction=='down':
        if __can_move(snake, snake.x, snake.y+1):
         snake.y+=1
    elif snake.direction=='up':
        if __can_move(snake, snake.x, snake.y-1):
            snake.y-=1  

    return snake




### move body       //     game over if head doesn't move      //    snake grow if eat rabbits
def move_body(snake, snake1):
    # кролик
    if snake1.matrix[snake.y][snake.x]==2:
        snake.snake_body[len(snake.snake_body)+1]=snake.snake_body[len(snake.snake_body)]
        snake1.delete_rabbit(snake.x, snake.y)

    # двигает хвост змеи на 1 вперед
    for i in range(len(snake.snake_body), 1, -1):
        snake.snake_body[i]=snake.snake_body[i-1] 

    # врезается в себя
    for i in range(2, len(snake.snake_body)+1):
        if snake.snake_body[i]==[snake.x, snake.y]: 
            if snake.second_snake==False:
                snake.scene='game over'
                
            else:
                snake.scene='dead'
        snake.snake_body[1]=[snake.x, snake.y]

    # врезается в другую змею
    if snake.second_snake==False:
        if len(snake.snakes_list)>1:
            for i in snake.snakes_list:
                if i!=snake:
                    for j in range(1, len(i.snake_body)+1):
                        if i.snake_body[j]==[snake.x, snake.y]: 
                            snake.scene='game over'
                            

    else:
        if len(snake1.snakes_list)>2:
            for i in snake1.snakes_list:
                if i!=snake:
                    for j in range(1, len(i.snake_body)+1):
                        if i.snake_body[j]==[snake.x, snake.y]: 
                            snake.scene='dead'

        for j in range(1, len(snake1.snake_body)+1):
            if snake1.snake_body[j]==[snake.x, snake.y]: 
                snake.scene='dead'

    snake.num_matrix=[[ 0 for i in range(40)] for _ in range(40)] 

    return snake, snake1



### can move if 0 or rabbit//cant move back
def __can_move(snake, new_x, new_y): 
    if snake.matrix[new_y][new_x]==0 or snake.matrix[new_y][new_x]==2:
        if snake.snake_body[2]==[new_x, new_y]:
            return False
        return True
    else:
        return False








### auto snake
def auto_move_snake(snake):
    try:

        if snake.path[1][1]<snake.x:
            if snake.direction!='right':
                snake=rotate_snake(snake, 'left')
            else:
                snake=rotate_snake(snake, 'down')
        elif snake.path[1][1]>snake.x:
            if snake.direction!='left':
                snake=rotate_snake(snake, 'right')
            else:
                snake=rotate_snake(snake, 'up')
        elif snake.path[1][0]<snake.y:
            if snake.direction!='down':
                snake=rotate_snake(snake, 'up')
            else:
                snake=rotate_snake(snake, 'left')
        elif snake.path[1][0]>snake.y:
            if snake.direction!='up':
                snake=rotate_snake(snake, 'down')
            else:
                snake=rotate_snake(snake, 'right')
    except:
        pass

    return snake




















