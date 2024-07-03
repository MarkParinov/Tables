import os

if os.path.exists('./tables'):
    print("Data table creating system engaged. Tables folder exists, ready to use. Type 'help' for command list.")
else:
    os.mkdir('./tables')
    print("Data table creating system engaged. Tables folder created, ready to use. Type 'help' for command list.")

cur_table = ''

def newTable(new_table_name):
    os.mkdir(f'./tables/{new_table_name}')
    new_path = f'./tables/{new_table_name}'
    open(f'./tables/{new_table_name}/content', 'w')
    open(f'./tables/{new_table_name}/content', 'w').close()
    print('Table created.')

def openTable():

    global cells
    global cur_table
    global table_name
    global list_splitted

    cells = []

    list_fold = os.listdir('./tables/')
    if list_fold == []:
        print('No existing tables. Create a table first.')
        return
    for i in range(len(list_fold)):
        print('\n---' + list_fold[i])
    print('\nChoose a table to open')
    table_name = input('>>')
    try:
        cur_table = open(f'./tables/{table_name}/content', 'r+', encoding='UTF-8')
        print('Table opened.')
        list_splitted = cur_table.read().split(' ')
        for i in range(len(list_splitted)):
            cells.append(list_splitted[i].split('|'))

        cur_table.close()
    except:
        print("An error occured while opening a table.")

    

    

def newCell(cell_cont, cell_row, cell_col):

    global cells
    global cur_table

    first_cell = True

    for i in range(len(cells)):

        if cell_row in cells[i] and cell_col in cells[i]:
            print("Cell with same row and column already exists. Please, try different row and column values.")
            return

    cells.append([cell_cont, cell_row, cell_col])
    print('Do you want for this cell to be saved in the current table? Y/N')
    inp = input()
    cur_table_a = open(f'./tables/{table_name}/content', 'a+', encoding='UTF-8')
    list_splitted = cur_table_a.read().split(' ')
    print(len(list_splitted))
    print(list_splitted)
    if inp == 'Y':
        if len(list_splitted) <= 0:
            add_cells = f'{cell_cont}|{cell_row}|{cell_col}'
            cur_table_a.write(add_cells)
        elif len(list_splitted) > 0:
            add_cells = f' {cell_cont}|{cell_row}|{cell_col}'
            cur_table_a.write(add_cells)
    elif inp =='N':
        return
    else: 
        print('No such option.')
    cur_table_a.close()
    print(cells)

def renderTable():

    global cells

    cols = []
    rows = []
    row_max = ''
    sep = ''
    cell_max = ''

    try:

        for i in range(len(cells)):
            if cells[i][2] not in cols:
                cols += [cells[i][2]]
            if cells[i][1] not in rows:
                rows += [cells[i][1]]

        for i in range(len(cells)):
            if len(cells[i][0]) > len(cell_max):
                cell_max = cells[i][0]

        for i in range(len(rows)):
            if len(rows[i]) > len(row_max):
                row_max = rows[i]

        cols_name = cols[:]

        for i in range(len(cols)):
            for n in range(len(cells)):
                if len(cells[n][0]) > len(cols[i]):
                    cols[i] += " " * (len(cells[n][0]) - len(cols[i]))
                if len(cells[n][0]) < len(cols[i]):
                    cells[n][0] += " " * (len(cols[i]) - len(cells[n][0]))

        sep += '-' * (len(row_max) + 1)

        print(' ' * (len(row_max) + 1), end = '')
        for i in range(len(cols)):
            print('|' + cols[i], end = '')
            sep += '+'
            sep += '-' * len(cols[i])
        print('|')
        sep += '+'

        for i in range(len(rows)):
            out = ''
            out += rows[i]
            out += ' ' * (len(row_max) - len(rows[i]) + 1)
            out += '|'

            cur_row = rows[i]
            
            for n in range(len(cols_name)):

                fill_cell = False
                filled = False

                cur_col = cols_name[n]
                
                for f in range(len(cells)):

                    if len(cells[f][0]) < len(cell_max):
                        fill_cell = True

                    if cells[f][1] == cur_row and cells[f][2] == cur_col and fill_cell == True:
                        out += cells[f][0]
                        out += ' ' * (len(cell_max) - len(cells[f][0]))
                        out += '|'
                        filled = True
                    
                    elif cells[f][1] == cur_row and cells[f][2] == cur_col and fill_cell == False:
                        out += cells[f][0]
                        out += '|'
                        filled = True

                if filled != True:
                    out += " " * len(cell_max)
                    out += '|'

            print(sep)
            print(out)
    except:
        print("Error. Make sure you have a table opened and it contains cells to render.")

while True:
    com_exc = False
    inp = input('>')

    if inp == 'help':
        print(' >>> newTable -- creates a new table in a default tables folder.')
        print(' >>> openTable -- opens a new table in a default tables folder.')
        print(' >>> newCell -- adds a cell to an opened table.')
        print(' >>> renderTable -- renders opened table with defaault text.')
        print(' >>> softwareInfo -- qucik description of the program.')
        com_exc = True
    if inp == 'softwareInfo':
        print('This is a simple program for creating, rendering and editing one-dimensional tables. Made on Python with default libraries. This is an independent project, source code can be found on my github. If you are reading this, I probably published it online as a full software.\nStill in development.')
        com_exc = True
    if inp == 'newCell':
        if cur_table == '':
            print('Error. Please, open a table to work in.')
        else:
            newCell(input('Cell conent: '), input('Cell row: '), input('Cell column: '))
        com_exc = True
    if inp == 'renderTable':
        com_exc = True
        renderTable()
    if inp == 'openTable':
        openTable()
        com_exc = True
    if inp == 'newTable':
        newTable(input('Enter new table name: '))
        com_exc = True
    if com_exc == False:
        print("No such command")