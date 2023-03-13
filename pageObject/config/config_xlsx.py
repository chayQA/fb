import xlrd

class ConfigXlsxData:
    #open_workbook will open the entire excel file
    book = xlrd.open_workbook(r'C:\Users\chaitanya\OneDrive - Universal Institute of Technology\Desktop\python\readexcel.xlsx')


    #sheet_by_name() it take one argument (str) the sheet name which we need to read
    sheet1 = book.sheet_by_name('Sheet1')
    #sheet1 = book.sheet_by_name(0)

    # nrows is function which is not callable it will return number of rows
    row_count = sheet1.nrows

    # ncols is function which is not callable it will return number of columns
    col_count = sheet1.ncols

    print ("the value of rows and coloums is : {0}". format(sheet1.cell(0,0).value))

