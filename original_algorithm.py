import curses
import datetime
import random



# find path
def find_path1(self, snake1): # -screen, self
    matrix=snake1.matrix

    num_matrix = [[ 0 for i in range(40)] for _ in range(40)]

    # borders
    for l in range(len(matrix)):
        for j in range(len(matrix[l])):
            if matrix[l][j]==1:
                num_matrix[l][j]=999

    # rabbit
    for l in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[l][j]==2:
                num_matrix[l][j]=998
                end_x=j
                end_y=l

    # snake body
    body=0
    a1, b1=0, 0
    for i in range(1, len(self.snake_body)+1):
        if self.snake_body[i][1]>self.y: # расстояние y
            a1=self.snake_body[i][1]-self.y 
        else:
            a1=self.y-self.snake_body[i][1] 
        if self.snake_body[i][0]>self.x: # расстояние x
            b1=self.snake_body[i][0]-self.x 
        else:
            b1=self.x-self.snake_body[i][0] 

        body=len(self.snake_body)+1-i # через сколько шагов хвост пропадет

        if body>=a1 and body>=b1:
            num_matrix[self.snake_body[i][1]][self.snake_body[i][0]]=999


    # other snake body
    other_snake=0
    if self.second_snake==False:
        pass
    else:
        other_snake=snake1.snake_body
        num_matrix[snake1.y][snake1.x]=999

        for j in range(1, len(other_snake)+1):
                if other_snake[j][1]>self.y: # расстояние y
                    a1=other_snake[j][1]-self.y 
                else:
                    a1=self.y-other_snake[j][1] 
                if other_snake[j][0]>self.x: # расстояние x
                    b1=other_snake[j][0]-self.x 
                else:
                    b1=self.x-other_snake[j][0] 

                body=len(other_snake)+1-j # через сколько шагов хвост пропадет

                if body>=a1 and body>=b1:
                    num_matrix[other_snake[j][1]][other_snake[j][0]]=999     

    for i in snake1.snakes_list:
        if i!=self:
            other_snake=i.snake_body
            num_matrix[i.y][i.x]=999   
            for j in range(1, len(other_snake)+1):
                if other_snake[j][1]>self.y: # расстояние y
                    a1=other_snake[j][1]-self.y 
                else:
                    a1=self.y-other_snake[j][1] 
                if other_snake[j][0]>self.x: # расстояние x
                    b1=other_snake[j][0]-self.x 
                else:
                    b1=self.x-other_snake[j][0] 

                body=len(other_snake)+1-j # через сколько шагов хвост пропадет

                if body>=a1 and body>=b1:
                    num_matrix[other_snake[j][1]][other_snake[j][0]]=999                                  

   




    # snake head
    num_matrix[self.y][self.x]=1

    pathfound=False
    pathnotfound=False
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
        if num>100:
            pathnotfound=True
            pathfound=True




    # на пути хвост
    if pathnotfound==True:
        # поиск пути к наибольшему значению (самой дальней клетке)
        max_num=0
        for i in range(len(num_matrix)):
            for j in range(len(num_matrix[i])):
                if num_matrix[i][j]>max_num and num_matrix[i][j]<998:
                    max_num=num_matrix[i][j]
                    end_y=i
                    end_x=j



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

        if num_matrix[l][j]>1 and num_matrix[l][j]<999:
            a.append(num_matrix[l][j])
            b.append([l, j])

        if len(a)==0:
            path[1]=[end_y, end_x]
        else:
            path[i] = b[a.index(min(a))]
            l = b[a.index(min(a))][0]
            j = b[a.index(min(a))][1]  
    if len(path)==0:
        path[1]=[end_y, end_x]

  

    #txt robot snake path
    f=open('robot_snake_path.txt', 'a')
    f.write('\n'+str(datetime.datetime.now())+'\n'+'\n')
    f.write('\n'+str(path)+'\n')
    f.write('\n'+str(len(self.snake_body))+'\n')
    for i in num_matrix:
        f.write(str(i)+'\n')

    return path









