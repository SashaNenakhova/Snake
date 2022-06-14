import curses


x = 15 # left, right
y = 15 # up, down
matrix = [[ 0 for i in range(30)] for _ in range(30)]
matrix[25][10]=2 #rabbit
snake_body={i:[x, y+i-1] for i in range(1, 12)}


# ------------------------------------------------------------------------------------------------------------------


def find_path(matrix): # -screen, self
        num_matrix = [[ 0 for i in range(30)] for _ in range(30)]


        # borders
        for l in range(len(matrix)):
                for j in range(len(matrix[l])):
                    if l==0 or l==len(matrix)-1 or j==0 or j==len(matrix[l])-1:
                        num_matrix[l][j]=999

        # rabbit
        for l in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[l][j]==2:
                    num_matrix[l][j]=998
                    end_x=j
                    end_y=l

        # snake body
        body=len(snake_body)//2
        for i in range(1, len(snake_body)+1):
            if body>=(snake_body[i][0]-body) or body>=(body-snake_body[i][0]) or body>=(snake_body[i][1]-body) or body>=(body-snake_body[i][1]):
                num_matrix[snake_body[i][1]][snake_body[i][0]]=999

        # snake head
        num_matrix[y][x]=1

        pathfound=False
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


            # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            print('num', num, 'value', value, 'found -', found, 'pathfound -', pathfound)
            print(num_matrix[l-1][j],
                num_matrix[l+1][j],
                num_matrix[l][j-1],
                num_matrix[l][j+1])
            for i in num_matrix:
                print(i)

            num+=1



        ### finding path ###


#____________________________________________________________________________________________________________


        
        # numbered matrix, end x, end y >>>> path
        # path lenght = num
        path, j, l= {}, end_x, end_y
        for i in range(num-3, 0, -1):

            a = [] # список значений из numbered matrix
            l = [] # список соответствующих им координат
            if num_matrix[l - 1][j] != 0 and num_matrix[l - 1][j] < 999:
                a.append(num_matrix[l - 1][j])
                l.append([l - 1, j])

            if num_matrix[l + 1][j] != 0 and num_matrix[l + 1][j] < 999:
                a.append(num_matrix[l + 1][j])
                l.append([l + 1, j])

            if num_matrix[l][j - 1] != 0 and num_matrix[l][j - 1] < 999:
                a.append(num_matrix[l][j - 1])
                l.append([l, j - 1])

            if num_matrix[l][j + 1] != 0 and num_matrix[l][j + 1] < 999:
                a.append(num_matrix[l][j + 1])
                l.append([l, j + 1])

            path[i] = l[a.index(min(a))]
            l = l[a.index(min(a))]
            j = l[a.index(min(a))]
        if len(path)==0:
            path=[end_y, end_x]

        print(path)
        # return path

# ------------------------------------------------------------------------------------------------------------------------

        # ## draw matrix
        # for i in range(len(numbered_matrix)):
        #     for j in range(len(numbered_matrix[i])):
        #         self.screen.move(5 + i, 5 + j * 2)
        #         if numbered_matrix[i][j][1] == 0:
        #             self.screen.addstr('  ', curses.color_pair(10))
        #         elif numbered_matrix[i][j][1] == 999:
        #             self.screen.addstr('  ', curses.color_pair(1))
        #         elif numbered_matrix[i][j][1] == 998:
        #             self.screen.addstr('  ', curses.color_pair(4))
        #         else:
        #             self.screen.addstr(str(numbered_matrix[i][j][1])+' ')
        # ## draw path
        # for i in range(1, len(path)+1):
        #     self.screen.move(5+path[i][0], 5+path[i][1]*2)
        #     self.screen.addstr('  ', curses.color_pair(2))
        # ## draw snake body
        # for i in range(0, len(path_snake_body)):
        #     self.screen.move(5  + path_snake_body[i][1], 5 + path_snake_body[i][2] * 2)
        #     self.screen.addstr(str(path_snake_body[i][0]+2), curses.color_pair(16))

        # self.screen.addstr(1, 1, str(path_snake_body))

# -----------------------------------------------------------------------------------------------------------------




find_path(matrix)








