import csv
import xlrd
import xlwt
# 读取csv至字典
csvFile = open("../ACS_10_5YR_DP02/ACS_10_5YR_DP02_metadata.csv", "r")
reader = csv.reader(csvFile)
csvFile1 = open("../ACS_10_5YR_DP02/ACS_10_5YR_DP02_with_ann.csv", "r")
reader1 = csv.reader(csvFile1)
row = []
row_name = []
for it in reader1:
    row = it
    break
row_name = next(reader1)

result = []
Y = []
index = []
year = []
id = []
for item in reader:
    if reader.line_num <= 3:
        continue
    if item[0][2:4] != "01":
        continue
    for j in range(len(row)):
        if row[j] == item[0]:
            index.append(j)
            break
print(index)
workbook = xlrd.open_workbook('MCM_NFLIS_Data.xlsx')
booksheet = workbook.sheet_by_index(1)
row_num = booksheet.nrows

csvFile1 = open("../ACS_10_5YR_DP02/ACS_10_5YR_DP02_with_ann.csv", "r")
reader1 = csv.reader(csvFile1)
for it1 in reader1:
    re = []
    if reader1.line_num < 3:
        continue
    for i in range(len(index)):
        re.append(it1[index[i]])
    result.append(re)
    id.append(it1[1])
    del re
    find = False
    for i in range(row_num):
        row = booksheet.row_values(i)
        if row[5] == it1[1]:
            Y.append(row[8])
            del row
            find = True
            break
    if not find:
        Y.append(500)
    year.append(2010)

csvFile2 = open("../ACS_11_5YR_DP02/ACS_11_5YR_DP02_with_ann.csv", "r")
reader2 = csv.reader(csvFile2)
for it2 in reader2:
    re = []
    if reader2.line_num < 3:
        continue
    for i in range(len(index)):
        re.append(it2[index[i]])
    result.append(re)
    id.append(it2[1])
    del re
    find = False
    for i in range(row_num):
        row = booksheet.row_values(i)
        if row[5] == it2[1]:
            Y.append(row[8])
            del row
            find = True
            break
    if not find:
        Y.append(500)
    year.append(2011)

csvFile3 = open("../ACS_12_5YR_DP02/ACS_12_5YR_DP02_with_ann.csv", "r")
reader3 = csv.reader(csvFile3)
for it3 in reader3:
    re = []
    if reader3.line_num < 3:
        continue
    for i in range(len(index)):
        re.append(it3[index[i]])
    result.append(re)
    id.append(it3[1])
    del re
    find = False
    for i in range(row_num):
        row = booksheet.row_values(i)
        if row[5] == it3[1]:
            Y.append(row[8])
            del row
            find = True
            break
    if not find:
        Y.append(500)
    year.append(2012)

csvFile4 = open("../ACS_13_5YR_DP02/ACS_13_5YR_DP02_with_ann.csv", "r")
reader4 = csv.reader(csvFile4)
for it4 in reader4:
    re = []
    if reader4.line_num < 3:
        continue
    for i in range(len(index)):
        re.append(it4[index[i]])
    result.append(re)
    id.append(it4[1])
    del re
    find = False
    for i in range(row_num):
        row = booksheet.row_values(i)
        if row[5] == it4[1]:
            Y.append(row[8])
            del row
            find = True
            break
    if not find:
        Y.append(500)
    year.append(2013)

csvFile5 = open("../ACS_14_5YR_DP02/ACS_14_5YR_DP02_with_ann.csv", "r")
reader5 = csv.reader(csvFile5)
for it5 in reader5:
    re = []
    if reader5.line_num < 3:
        continue
    for i in range(len(index)):
        re.append(it5[index[i]])
    result.append(re)
    id.append(it5[1])
    del re
    find = False
    for i in range(row_num):
        row = booksheet.row_values(i)
        if row[5] == it5[1]:
            Y.append(row[8])
            del row
            find = True
            break
    if not find:
        Y.append(500)
    year.append(2014)

csvFile6 = open("../ACS_15_5YR_DP02/ACS_15_5YR_DP02_with_ann.csv", "r")
reader6 = csv.reader(csvFile6)
for it6 in reader6:
    re = []
    if reader6.line_num < 3:
        continue
    for i in range(len(index)):
        re.append(it6[index[i]])
    result.append(re)
    id.append(it6[1])
    del re
    find = False
    for i in range(row_num):
        row = booksheet.row_values(i)
        if row[5] == it6[1]:
            Y.append(row[8])
            del row
            find = True
            break
    if not find:
        Y.append(500)
    year.append(2015)

csvFile7 = open("../ACS_16_5YR_DP02/ACS_16_5YR_DP02_with_ann.csv", "r")
reader7 = csv.reader(csvFile7)
for it7 in reader7:
    re = []
    if reader7.line_num < 3:
        continue
    for i in range(len(index)):
        re.append(it7[index[i]])
    result.append(re)
    id.append(it7[1])
    del re
    find = False
    for i in range(row_num):
        row = booksheet.row_values(i)
        if row[5] == it7[1]:
            Y.append(row[8])
            del row
            find = True
            break
    if not find:
        Y.append(500)
    year.append(2016)

avg = []
for i in range(len(index)):
    sum = 0
    num = 0
    for j in range(len(result)):
        if result[j][i] != "**" and result[j][i] != "-" and result[j][i] != "+" \
                and result[j][i] != "***" and result[j][i] != "*****" and result[j][i] != "(X)":
            sum += float(result[j][i])
            num += 1
    if num == 0:
        avg.append(0)
        continue
    avg.append(sum/num)

for i in range(len(index)):
    for j in range(len(result)):
        if result[j][i] != "**" and result[j][i] != "-" and result[j][i] != "+" \
                and result[j][i] != "***" and result[j][i] != "*****" and result[j][i] != "(X)":
            result[j][i] = float(result[j][i])
        else:
            result[j][i] = avg[i]
        Y[j] = float(Y[j])

csvFile.close()
csvFile1.close()
csvFile2.close()
csvFile3.close()
csvFile4.close()
csvFile5.close()
csvFile6.close()
csvFile7.close()
print(result)
workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('My Worksheet')
for i in range(len(result)):
    if i == 0:
        worksheet.write(i, 0, label="id")
        worksheet.write(i, 1, label="total_num_drug")
        worksheet.write(i, 2, label="year")
        for j in range(3, 3 + len(index)):
            worksheet.write(i, j, label=row_name[index[j - 3]])
        continue
    worksheet.write(i, 0, label=id[i])
    worksheet.write(i, 1, label=Y[i])
    worksheet.write(i, 2, label=year[i])
    for j in range(3, 3 + len(index)):
        worksheet.write(i, j, label=result[i][j - 3])
workbook.save('Workbook.xls')
