import xlrd

loc = ("E:\\DataScienceLearningProcess\\DatascienceStudy_plan.xlsx")

wb = xlrd.open_workbook(loc)

sheet= wb.sheet_by_index(0)

print(sheet.ncols)
print(sheet.nrows)