import curses
import datetime
import random



# find path
def find_path2(self, snake1): # -screen, self
    self.num_matrix = [[ 0 for i in range(40)] for _ in range(40)]
    matrix=snake1.matrix

    # rabbit
    for l in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[l][j]==2:
                snake1.num_matrix[l][j]=1


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
                        if snake1.num>50:
                            pathfound=True


                        # увеличить значение в центральной клетке до наименьшего+1
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



    # second snakes matrix (snakes bodies + snake1.num_matrix)
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

    return path






