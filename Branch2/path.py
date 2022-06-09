
x=15
y=15
snake_body={i:[x, y+i-1] for i in range(1, 8)}
snake_head = [[0]]

matrix = [[ 0 for i in range(30)] for _ in range(30)]
## add borders
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==0 or i==len(matrix)-1 or j==0 or j==len(matrix[i])-1:
            matrix[i][j]=1
matrix[2][3]=2 #rabbit

####################################################################################################


def find_path(screen, matrix, x, y):
    numbered_matrix=[[ [0, 0] for i in range(30)] for _ in range(30)]
    num = 1
    pathfound = False
    end_y, end_x = 0, 0

    # [0, number] - empty
    # [1, 999] - wall
    # [3, 998] - rabbit
    # [2, 1] - snake head
    # numbered_matrix[x][y]=[type, value]

    # set end x, end y, borders
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                numbered_matrix[i][j]=[1,999] # border
            elif matrix[i][j]==2: # rabbit
                end_y, end_x=i, j


    # number snake body
    path_snake_body=[[i, snake_body[i][1], snake_body[i][0]] for i in range(2, len(snake_body)+1)]
    for i in range(2, len(path_snake_body)+2):
        path_snake_body[i-2][0]=len(path_snake_body)+1-i


    ###  добавиь в numbered_matrix тип тело змеи со значениями path_snake_body
    for i in path_snake_body:
        numbered_matrix[i[1]][i[2]]=[2, i[0]+len(snake_body)]


    # set snake head, rabbit
    numbered_matrix[y][x]=[2, 1] #head
    numbered_matrix[end_y][end_x]=[3, 998] # rabbit

    # num, end_x, end_y >>>> numbered matrix
    while pathfound == False:
        # проходим матрицу и заполняем её значениями дистанции от стартовой точки
        for l in range(len(numbered_matrix)):
            for j in range(len(numbered_matrix[l])):

                if (numbered_matrix[l][j][1] == 0 or numbered_matrix[l][j][1]==998):
                    # надо определить, есть ли в ближайшем окружении заполненные ячейки, и, если есть, выбрать среди них наименьшую

                    found = False
                    value = 999


                    # up
                    if (numbered_matrix[l - 1][j][1] <= 998) and (numbered_matrix[l - 1][j][1] > 0):
                        found = True
                        if numbered_matrix[l - 1][j][1] < value:
                            value = numbered_matrix[l - 1][j][1]
                    # down
                    if (numbered_matrix[l + 1][j][1] <= 998) and (numbered_matrix[l + 1][j][1] > 0):
                        found = True
                        if numbered_matrix[l + 1][j][1] < value:
                            value = numbered_matrix[l + 1][j][1]
                    # left
                    if (numbered_matrix[l][j - 1][1] <= 998) and (numbered_matrix[l][j - 1][1] > 0):
                        found = True
                        if numbered_matrix[l][j - 1][1] < value:
                            value = numbered_matrix[l][j - 1][1]
                    # right
                    if (numbered_matrix[l][j + 1][1] <= 998) and (numbered_matrix[l][j + 1][1] > 0):
                        found = True
                        if numbered_matrix[l][j + 1][1] < value:
                            value = numbered_matrix[l][j + 1][1]

                    # adding numbers to matrix
                    if (found == True) and (value < num):
                        numbered_matrix[l][j][1] = value + 1

                    # уменьшить значения змеи
                    if numbered_matrix[l][j][0]==2:
                        numbered_matrix[l][j][1]-=1


                    # found rabbit
                    if numbered_matrix[end_y][end_x][1]==value+1 and found==True:
                        pathfound = True
        num += 1







    # numbered matrix, end x, end y >>>> path
    # path lenght = num
    path, path_j, path_l= {}, end_x, end_y
    for i in range(num-3, 0, -1):

        a = [] # список значений из numbered matrix
        l = [] # список соответствующих им координат
        if numbered_matrix[path_l - 1][path_j][1] != 0 and numbered_matrix[path_l - 1][path_j][1] < 999:
            a.append(numbered_matrix[path_l - 1][path_j][1])
            l.append([path_l - 1, path_j])
        if numbered_matrix[path_l + 1][path_j][1] != 0 and numbered_matrix[path_l + 1][path_j][1] < 999:
            a.append(numbered_matrix[path_l + 1][path_j][1])
            l.append([path_l + 1, path_j])
        if numbered_matrix[path_l][path_j - 1][1] != 0 and numbered_matrix[path_l][path_j - 1][1] < 999:
            a.append(numbered_matrix[path_l][path_j - 1][1])
            l.append([path_l, path_j - 1])
        if numbered_matrix[path_l][path_j + 1][1] != 0 and numbered_matrix[path_l][path_j + 1][1] < 999:
            a.append(numbered_matrix[path_l][path_j + 1][1])
            l.append([path_l, path_j + 1])

        path[i] = l[a.index(min(a))]
        path_l = l[a.index(min(a))][0]
        path_j = l[a.index(min(a))][1]

    if len(path)==0:
        path[1]=[end_y, end_x]


    ## draw matrix
    for i in range(len(numbered_matrix)):
        for j in range(len(numbered_matrix[i])):
            screen.move(5 + i, 5 + j * 2)
            if numbered_matrix[i][j][1] == 0:
                screen.addstr('  ', curses.color_pair(10))
            elif numbered_matrix[i][j][1] == 999:
                screen.addstr('  ', curses.color_pair(1))
            elif numbered_matrix[i][j][1] == 998:
                screen.addstr('  ', curses.color_pair(4))
            else:
                screen.addstr(str(numbered_matrix[i][j][1])+' ')

    ## draw path
    for i in range(1, len(path)+1):
        screen.move(5+path[i][0], 5+path[i][1]*2)
        screen.addstr('  ', curses.color_pair(2))

    ## draw snake body
    for i in range(0, len(path_snake_body)):
        screen.move(5  + path_snake_body[i][1], 5 + path_snake_body[i][2] * 2)
        screen.addstr(str(path_snake_body[i][0]+2), curses.color_pair(16))

    screen.addstr(1, 1, str(path_snake_body))

    return path










### auto snake
def auto_move_snake(self):
        path=find_path(screen, matrix, x, y)

        if path[1][1]<x:
            if self.direction!='right':
                self.rotate_snake('left')
                self.screen.addstr(40, 10, 'left')
            else:
                self.rotate_snake('down')
        if path[1][1]>x:
            if self.direction!='left':
                self.rotate_snake('right')
                self.screen.addstr(40, 10, 'right')
            else:
                self.rotate_snake('up')
        if path[1][0]<y:
            if self.direction!='down':
                self.rotate_snake('up')
                self.screen.addstr(40, 10, 'up')
            else:
                self.rotate_snake('left')
        if path[1][0]>y:
            if self.direction!='up':
                self.rotate_snake('down')
                self.screen.addstr(40, 10, 'down')
            else:
                self.rotate_snake('right')



























