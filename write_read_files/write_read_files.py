import csv
import xlrd

#возвращает матрицу(список) считанный
def parse_xml(file, start_row=1, start_sheet=1):
    rb = xlrd.open_workbook(file)
    sheet = rb.sheet_by_index(start_sheet)
    matrix = []
    #start_row = 1
    i = start_row
    for rownum in range(start_row, sheet.nrows):
        row = sheet.row_values(rownum)
        matrix_row = []
        j = 0
        for c_el in row:
            if c_el == "":
                if i == start_row:
                    c_el = find_value(sheet, i, j)
                else:
                    # c_el = sheet.row_values(i-1)[j]
                    c_el = matrix[i-2][j]
            matrix_row.append(float(c_el))
            if c_el == '':
                raise TypeError
            j += 1
        matrix.append(matrix_row)
        i += 1
    return matrix

def find_value(sheet,i,j):
    c_el = ''
    #ищем значение такого же столбца в других строках
    for rownum in range(i+1, sheet.nrows):
        row = sheet.row_values(rownum)
        if row[j] != '':
            c_el = row[j]
    #если не нашли ищем во всех остальных
    if c_el == '':
        for rownum in range(i+1, sheet.nrows):
            row = sheet.row_values(rownum)
            for c in row:
                if c !='':
                    c_el = c
                    break
            if c_el != '':
                break
    return c_el

def parse_csv(file):
        matrix=[]
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                r=[]
                for cell in row:
                    r.append(float(cell))
                matrix.append(r)
        return matrix

def write_csv_list(file,matrix):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(matrix)