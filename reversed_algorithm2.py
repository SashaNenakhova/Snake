import curses
import datetime
import random
from draw_snake_game import *               #draw, draw_menu, draw_game
from move_snake import *                    #rotate_snake, move_head, move_body, __can_move, auto_move_snake
from records_functions import *             #update_file, read_file, add_records, clear_records
from get_input import *                     #getinput




def path_not_found(snake):
    snake.num_matrix[snake.y][snake.x]=1
    num=0
    while num<30:
        for l in range(1, len(snake.num_matrix)-1):
            for j in range(1, len(snake.num_matrix[l])-1):
                if snake.num_matrix[l][j]==998 or snake.num_matrix[l][j]==0:
                    # надо определить, есть ли в ближайшем окружении заполненные ячейки, и, если есть, выбрать среди них наименьшую
                    found = False # если не найдено заполненых клеток
                    value=999
                    ## поиск клеток со значением больше 0; не стены
                    ## поиск наименьшего значения (расстояния от кролика)
                    # верхняя клетка
                    if snake.num_matrix[l-1][j]<998 and snake.num_matrix[l-1][j]>0: 
                        found=True
                        if snake.num_matrix[l-1][j]<value: # поиск наименьшего значения 
                            value = snake.num_matrix[l-1][j]
                    # нижняя клетка
                    if snake.num_matrix[l+1][j]<998 and snake.num_matrix[l+1][j]>0: 
                        found=True
                        if snake.num_matrix[l+1][j]<value: # поиск наименьшего значения 
                            value = snake.num_matrix[l+1][j]
                    # левая клетка
                    if snake.num_matrix[l][j-1]<998 and snake.num_matrix[l][j-1]>0: 
                        found=True
                        if snake.num_matrix[l][j-1]<value: # поиск наименьшего значения 
                            value = snake.num_matrix[l][j-1]
                    # правая клетка
                    if snake.num_matrix[l][j+1]<998 and snake.num_matrix[l][j+1]>0: 
                        found=True
                        if snake.num_matrix[l][j+1]<value: # поиск наименьшего значения 
                            value = snake.num_matrix[l][j+1]
                    # увеличить значение в центральной клетке до наименьшего+1
                    # if found==True and value<snake1.num and snake1.num_matrix[l][j]==0:
                    if found==True and value<snake.num and snake.num_matrix[l][j]==0:
                        snake.num_matrix[l][j]=value+1
        num+=1
    snake.num_matrix[snake.y][snake.x]=998















## сюда попадает только основная змея
#### numbered matrix
def wave4(snake1):
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
            if snake_body[j][1]>snake1.y: # расстояние y
                a1=snake_body[j][1]-snake1.y 
            else:
                a1=snake1.y-snake_body[j][1] 
            if snake_body[j][0]>snake1.x: # расстояние x
                b1=snake_body[j][0]-snake1.x 
            else:
                b1=snake1.x-snake_body[j][0] 
            steps=len(snake_body)+1-j # через сколько шагов хвост пропадет
            if steps>=a1 and steps>=b1:
                snake1.num_matrix[snake_body[j][1]][snake_body[j][0]]=999  
            snake1.num_matrix[i.y][i.x]=998### 
    # snake head
    snake1.num_matrix[snake1.y][snake1.x]=998
    end_x=snake1.x
    end_y=snake1.y
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
                    if found==True and value<snake1.num and snake1.num_matrix[l][j]==0:
                        snake1.num_matrix[l][j]=value+1
                    # проверить если путь найден
                    for i in snake1.snakes_list:
                        if l==i.y and j==i.x and found==True:
                            i.wave_algorithm=True
                            i.num=snake1.num
                    for i in snake1.snakes_list:
                        if i.wave_algorithm==False:
                            break
                    else:
                        pathfound=True
        snake1.num+=1
        if snake1.num>60 or snake1.count_rabbits==0:
            pathnotfound=True
            pathfound=True

    if snake1.wave_algorithm==False and snake1.count_rabbits>0: ###
        snake1.path_not_found()

    for i in snake1.snakes_list:
        i.wave_algorithm=False
    snake1.find_path_x, snake1.find_path_y=end_x, end_y














# find path
def find_path4(snake, snake1):

    j, l=snake.x, snake.y 
    if snake!=snake1:
        for i in range(len(snake1.num_matrix)):
            for t in range(len(snake1.num_matrix[i])):
                if snake1.num_matrix[i][t]<999:
                    snake.num_matrix[i][t]=snake1.num_matrix[i][t]
        # snake body
        steps=0
        a1, b1=0, 0
        snake_body=0 
        for i in snake1.snakes_list:
            snake_body=i.snake_body
            snake.num_matrix[i.y][i.x]=998   
            for k in range(1, len(snake_body)+1):
                if snake_body[k][1]>snake.y: # расстояние y
                    a1=snake_body[k][1]-snake.y
                else:
                    a1=snake.y-snake_body[k][1]
                if snake_body[k][0]>snake.x: # расстояние x
                    b1=snake_body[k][0]-snake.x
                else:
                    b1=snake.x-snake_body[k][0]
                steps=len(snake_body)+1-k # через сколько шагов хвост пропадет
                if steps>=a1 and steps>=b1:
                    snake.num_matrix[snake_body[k][1]][snake_body[k][0]]=999
        snake.num_matrix[snake.y][snake.x]=998

        for i in range(len(snake.num_matrix)):
            for k in range(len(snake.num_matrix[i])):
                if snake.num_matrix[i][k]==2:
                    if snake.x<=k:
                        snake.num=k-snake.x
                    else:
                        snake.num=snake.x-k
                    if snake.y<=i:
                        snake.num+=i-snake.y
                    else:
                        snake.num+=snake.y-i
                
    if snake!=snake1:
        f=open('robot_snake_path.txt', 'a')
        f.write(str(snake.num)+'  num'+ '\n'*2)
    # numbered matrix, end x, end y >>>> path
    # path lenght = num
    # j, l= end_x, end_y
    path={}
    for i in range(1, snake.num+1):
        a = [] # список значений из numbered matrix
        b = [] # список соответствующих им координат

        if snake.num_matrix[l - 1][j] >0 and snake.num_matrix[l - 1][j] < 998: # up
            a.append(snake.num_matrix[l - 1][j])
            b.append([l - 1, j])
        if snake.num_matrix[l + 1][j] >0 and snake.num_matrix[l + 1][j] < 998: # down
            a.append(snake.num_matrix[l + 1][j])
            b.append([l + 1, j])
        if snake.num_matrix[l][j - 1] >0 and snake.num_matrix[l][j - 1] <998: # left
            a.append(snake.num_matrix[l][j - 1])
            b.append([l, j - 1])
        if snake.num_matrix[l][j + 1] >0 and snake.num_matrix[l][j + 1] < 998: # right
            a.append(snake.num_matrix[l][j + 1])
            b.append([l, j + 1])
        if snake.num_matrix[l][j]>0 and snake.num_matrix[l][j]<998:
            a.append(snake.num_matrix[l][j])
            b.append([l, j])
        try:
            path[i] = b[a.index(min(a))]
            l = b[a.index(min(a))][0]
            j = b[a.index(min(a))][1]
        except:
            if snake.direction=='up':
                path[1]=[snake.y-1, snake.x]
            elif snake.direction=='down':
                path[1]=[snake.y+1, snake.x]
            elif snake.direction=='right':
                path[1]=[snake.y, snake.x+1]
            elif snake.direction=='left':
                path[1]=[snake.y, snake.x-1]
            break

    return path


