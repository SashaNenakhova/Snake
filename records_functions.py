
########### RECORDS ###########

### updating file
def update_file(snake):
    file = open('records.txt', 'w')
    strings = []
    # списки из records_top формируются в список строк
    for i in snake.records_top: 
        if len(i)==2:
            strings.append(i[0] + ';' + str(i[1]))
    # строки добавляются в конец файла
    for i in strings: 
        file.write(i+'\n')
    file.close()

### copy file to records_top
def read_file(snake):
    read=[]
    try:
        file=open('records.txt')
        str_list=file.read().split('\n')
        for i in str_list:
            if ';' in i:
                spl=i.split(';')
                read.append([spl[0], int(spl[1])])
    except FileNotFoundError:
        file = open('records.txt', 'w')
        file.write('')
    file.close()
    return read

### add record to records_top
def add_records(snake, record):
    if snake.records_top==[]:   # если список пустой
        snake.records_top.append(record)
    else:
        for i in range(len(snake.records_top)):
            if snake.records_top[i][1]<record[1]:  # если есть рекорд меньше
                snake.records_top.insert(i, record)
                break
        else:
            if len(snake.records_top)<10:  # если нет рекордов меньше но есть место в списке
                snake.records_top.append(record)

    if len(snake.records_top)==11:   # удаление лишних строк
        snake.records_top=snake.records_top[:-1]

    return snake

### clear records
def clear_records(snake):
    file=open('records.txt', 'w')
    file.write('')
    file.close()
    snake.records_top=[]

    return snake


