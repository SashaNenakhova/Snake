import curses
import random

def draw(matrix, path, screen, x, y):

    left_corner = (screen.getmaxyx()[1])//2 - len(matrix[0])-15 # ширина. 
    top_corner = (screen.getmaxyx()[0])//2 - len(matrix)//2 # высота. 

    ## matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            screen.move(top_corner+i, left_corner+j*2)
            if matrix[i][j]==0:
                screen.addstr('  ', curses.color_pair(10))
            elif matrix[i][j]==1:
                screen.addstr('  ', curses.color_pair(1))
            else:
                screen.addstr(' '+str(matrix[i][j]), curses.color_pair(0))

    ## head
    screen.move(top_corner+y, left_corner+x*2)
    screen.addstr('  ', curses.color_pair(2))

    ## rabbit
    screen.move(top_corner+28, left_corner+3*2)
    screen.addstr('  ', curses.color_pair(4))

    ## path
    for i in range(2, len(path)+1):
        screen.move(top_corner+path[i][0], left_corner+path[i][1]*2)
        screen.addstr('  ', curses.color_pair(20))


    screen.refresh()

def add_borders(matrix):
    ## borders
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==0 or i==len(matrix)-1 or j==0 or j==len(matrix[i])-1:
                matrix[i][j]=1


    for i in range(25):
        matrix[5+i][5]=1
    for i in range(20):
        matrix[5][5+i]=1
    for i in range(15):
        matrix[21-i][24]=1
    for i in range(15):
        matrix[22][24-i]=1
    for i in range(13):
        matrix[21-i][10]=1
    for i in range(10):
        matrix[9][20-i]=1
    for i in range(9):
        matrix[17-i][20]=1
    for i in range(7):
        matrix[18][20-i]=1


    return matrix









# wave algorithm/ find path
def find_path(screen, matrix, x, y):
    numbered_matrix=[[ 0 for i in range(30)] for _ in range(30)]
    num = 1
    pathfound = False

    # set end x, end y, borders
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                numbered_matrix[i][j]=999 # border
            elif matrix[i][j]==4: # rabbit
                end_y, end_x=i, j

    # set snake head, rabbit
    numbered_matrix[y][x]=1
    numbered_matrix[end_y][end_x]=998



    # num, end_x, end_y >>>> numbered matrix
    while pathfound == False:
        # проходим матрицу и заполняем её значениями дистанции от стартовой точки
        for l in range(len(numbered_matrix)):
            for j in range(len(numbered_matrix[l])):

                if numbered_matrix[l][j] == 0 or numbered_matrix[l][j]==998:
                    # надо определить, есть ли в ближайшем окружении заполненные ячейки, и, если есть, выбрать среди них наименьшую

                    found = False
                    value = 999

                    if (numbered_matrix[l - 1][j] < 998) and (numbered_matrix[l - 1][j] > 0):
                        found = True
                        if numbered_matrix[l - 1][j] < value:
                            value = numbered_matrix[l - 1][j]

                    if (numbered_matrix[l + 1][j] < 998) and (numbered_matrix[l + 1][j] > 0):
                        found = True
                        if numbered_matrix[l + 1][j] < value:
                            value = numbered_matrix[l + 1][j]

                    if (numbered_matrix[l][j - 1] < 998) and (numbered_matrix[l][j - 1] > 0):
                        found = True
                        if numbered_matrix[l][j - 1] < value:
                            value = numbered_matrix[l][j - 1]

                    if (numbered_matrix[l][j + 1] < 998) and (numbered_matrix[l][j + 1] > 0):
                        found = True
                        if numbered_matrix[l][j + 1] < value:
                            value = numbered_matrix[l][j + 1]

                    # adding numbers to matrix
                    if (found == True) and (value < num):
                        numbered_matrix[l][j] = value + 1


                    if numbered_matrix[l][j]==998 and found==True:
                        pathfound = True
        num += 1

    # numbered matrix, end x, end y >>>> path
    # path lenght = num
    path, path_j, path_l= {}, end_x, end_y
    for i in range(num - 1, 0, -1):

        a = []
        l = []
        if numbered_matrix[path_l - 1][path_j] != 0 and numbered_matrix[path_l - 1][path_j] < 999:
            a.append(numbered_matrix[path_l - 1][path_j])
            l.append([path_l - 1, path_j])
        if numbered_matrix[path_l + 1][path_j] != 0 and numbered_matrix[path_l + 1][path_j] < 999:
            a.append(numbered_matrix[path_l + 1][path_j])
            l.append([path_l + 1, path_j])
        if numbered_matrix[path_l][path_j - 1] != 0 and numbered_matrix[path_l][path_j - 1] < 999:
            a.append(numbered_matrix[path_l][path_j - 1])
            l.append([path_l, path_j - 1])
        if numbered_matrix[path_l][path_j + 1] != 0 and numbered_matrix[path_l][path_j + 1] < 999:
            a.append(numbered_matrix[path_l][path_j + 1])
            l.append([path_l, path_j + 1])

        path[i] = l[a.index(min(a))]
        path_l = l[a.index(min(a))][0]
        path_j = l[a.index(min(a))][1]

    return path









def main(screen):

    curses.start_color()
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_WHITE) # borders
    curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_BLACK) # black
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN) # head
    curses.init_pair(20, curses.COLOR_BLUE, curses.COLOR_BLUE) # path
    curses.init_pair(4, 0, 12*15) # rabbits

    # start:
    head_x=15
    head_y=15

    # end:
    # rabbit_x, rabbit_y = 25, 25


    matrix = [[ 0 for i in range(30)] for _ in range(30)]
    matrix = add_borders(matrix)
    matrix[28][3]=4 # rabbit

    path=find_path(screen, matrix, head_x, head_y)

    draw(matrix, path, screen, head_x, head_y)
    screen.getch()

    
    while True:
        draw(matrix, path, screen, head_x, head_y)


curses.wrapper(main)








