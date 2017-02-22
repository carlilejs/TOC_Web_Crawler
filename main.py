from urllib2 import urlopen
import xlrd

def get_product_numbers():
    sheet = xlrd.open_workbook('data/HBC_all_items_2016.xls').sheet_by_name('Sheet1')
    number_cells = sheet.col(1)
    return number_cells

product_numbers = []
for cell in get_product_numbers():
    product_numbers.append(cell.value)
