import numpy as np
import xlrd
import xlwt

result = []
di = {}
Di = {}

workbook = xlrd.open_workbook('MCM_NFLIS_Data.xlsx')
booksheet = workbook.sheet_by_index(1)
row_num = booksheet.nrows
num = 1
for i in range(1, row_num):
    row = booksheet.row_values(i)
    name = "di" + str(i)
    locals()[name] = {}
    locals()[name]["year"] = row[0]
    locals()[name]["name"] = row[2]
    locals()[name]["id"] = row[5]
    locals()[name]["num_drug"] = row[8]
    di["year"] = row[0]
    di["name"] = row[2]
    di["id"] = row[5]
    di["num_drug"] = row[8]
    if di not in Di.values():
        Di[num] = locals()[name]
        num = num + 1
    del locals()[name]

county = []
num_county = 0
for i in range(1, num):
    coun = Di[i]["id"]
    if coun not in county:
        county.append(coun)
        num_county = num_county + 1

N10_17 = []
N10_17.append([29588, 70999, 89981, 41462, 8668])
N10_17.append([28285, 71282, 86793, 28969, 9310])
N10_17.append([27502, 85415, 78577, 32251, 9429])
N10_17.append([26820, 93747, 72096, 47694, 9062])
N10_17.append([27077, 101423, 77318, 32265, 6926])
N10_17.append([25811, 109150, 75351, 27819, 5345])
N10_17.append([26530, 115276, 72376, 33539, 5405])
N10_17.append([28870, 119349, 68751, 36994, 3672])

array = np.zeros(shape=(5, 5))
for i in range(7):
    idx = 0
    m = N10_17[i][0]
    for j in range(5):
        if N10_17[i][j] > m:
            idx = j
            m = N10_17[i][j]
    for j in range(5):
        if j != idx:
            if N10_17[i+1][j] > N10_17[i][j] and array[idx, j] != 1:
                array[idx, j] = array[idx, j] + (N10_17[i+1][j] - N10_17[i][j])/N10_17[i][idx]
                # if array[idx, j] > 1:
                #     array[idx, j] = 1
            elif N10_17[i+1][j] < N10_17[i][j] and array[idx, j] != 0:
                array[idx, j] = array[idx, j] - (-N10_17[i+1][j] + N10_17[i][j])/N10_17[i][idx]
                # if array[idx, j] < 0:
                #     array[idx, j] = 0
array = array/7
array_state = array/7
array = np.zeros(shape=(num_county, num_county))
array = array*7
rate_state = 0.01
for i in range(num_county):
    for j in range(num_county):
        if county[i][0:2] == county[j][0:2]:
            array[i][j] = rate_state
        else:
            statei = statej = 0
            if county[i][0:2] == "21":
                statei = 0
            if county[i][0:2] == "39":
                statei = 1
            if county[i][0:2] == "42":
                statei = 2
            if county[i][0:2] == "51":
                statei = 3
            if county[i][0:2] == "54":
                statei = 4
            if county[j][0:2] == "21":
                statej = 0
            if county[j][0:2] == "39":
                statej = 1
            if county[j][0:2] == "42":
                statej = 2
            if county[j][0:2] == "51":
                statej = 3
            if county[j][0:2] == "54":
                statej = 4
            array[i, j] = array_state[statei, statej]

for i in range(7):
    idx = 1
    m = 0
    for j in range(1, len(Di)):
        if Di[j]["num_drug"] > m and Di[j]["year"] == i+2010:
            idx = j
            m = Di[j]["num_drug"]
        if Di[j]["year"] > i + 2011:
            break
    idx_county = 0
    for j in range(num_county):
        if county[j] == Di[idx]["id"]:
            idx_county = j
            break
    for j in range(num_county):
        if county[j] != Di[idx]["id"]:
            index1 = 0
            index2 = 0
            for k in range(1, len(Di)):
                if Di[k]["year"] == i + 2011 and Di[k]["id"] == county[j]:
                    index1 = k
                if Di[k]["year"] == i + 2010 and Di[k]["id"] == county[j]:
                    index2 = k
                if index1*index2 != 0:
                    break
                if Di[k]["year"] > i + 2011:
                    break
            if index1 * index2 != 0:
                array[idx_county, j] = array[idx_county, j] + (Di[index1]["num_drug"] - Di[index2]["num_drug"]) / \
                                Di[idx]["num_drug"]
array = array/7


def regre(year):
    reg = []
    for iin in range(num_county):
        s = 0
        s1 = 0
        s2 = 0
        s_year = 0
        num = 0
        for jin in range(year - 2010):
            inin = cal(iin, jin)
            if inin == 0:
                num += 1
            s += inin
            s_year += jin
        if year - 2010 - num == 0:
            avg_x = avg_y = 0
        else:
            avg_y = s / (year - 2010 - num)
            avg_x = s_year / (year - 2010 - num)
        for jin in range(year - 2010):
            if cal(iin, jin) != 0:
                s1 += (jin - avg_x) * (cal(iin, jin) - avg_y)
                s2 += (jin - avg_x) ** 2
        # b1 = (s1 - 8*13.5*avg_y)/(s2 - 8*(13.5**2))
        if s2 == 0:
            b1 = 0
        else:
            b1 = s1/s2
        b0 = avg_y - b1*avg_x
        y = b0 + b1*(year - 2010)
        reg.append(y)
    ma = 0
    indx = 0
    for iin in range(1, len(Di)):
        if Di[iin]["num_drug"] > ma and Di[iin]["year"] == year - 1:
            indx = iin
            ma = Di[iin]["num_drug"]
    indx_county = 0
    for iin in range(num_county):
        if Di[indx]["id"] == county[iin]:
            indx_county = iin
            break
    resultin = []
    for iin in range(num_county):
        ddi = {}
        if iin != indx_county:
            # now = cal(iin, year - 2011) + array[indx_county, iin]*Di[indx]["num_drug"]
            now = reg[iin] + array[indx_county, iin]*reg[indx_county]
            if now < 0:
                now = 0
            resultin.append(int(now))
            ddi["id"] = county[iin]
            ddi["year"] = year
            ddi["name"] = ""
            ddi["num_drug"] = now
            Di[len(Di) + 1] = ddi
            del ddi
        else:
            ddi["id"] = county[iin]
            ddi["year"] = year
            ddi["name"] = ""
            ddi["num_drug"] = reg[iin]
            Di[len(Di) + 1] = ddi
            del ddi
            resultin.append(int(reg[iin]))
    return resultin, indx


def cal(iin, jin):
    inin = 0
    for kin in range(1, len(Di)):
        if Di[kin]["id"] == county[iin] and Di[kin]["year"] == jin + 2010:
            inin = Di[kin]["num_drug"]
        # if Di[kin]["year"] > jin + 2018:
        #     inin = 0
    return inin


in1 = in2 = in3 = in4 = in5 = ""
name1 = name2 = name3 = name4 = name5 = ""
max1 = max2 = max3 = max4 = max5 = 0
for i in range(1, num_county):
    if Di[i]["year"] > 2010:
        break
    if Di[i]["num_drug"] > max1 and Di[i]["id"][0:2] == "21":
        in1 = Di[i]["id"]
        name1 = Di[i]["name"]
        max1 = Di[i]["num_drug"]
    if Di[i]["num_drug"] > max2 and Di[i]["id"][0:2] == "39":
        in2 = Di[i]["id"]
        name2 = Di[i]["name"]
        max2 = Di[i]["num_drug"]
    if Di[i]["num_drug"] > max3 and Di[i]["id"][0:2] == "42":
        in3 = Di[i]["id"]
        name3 = Di[i]["name"]
        max3 = Di[i]["num_drug"]
    if Di[i]["num_drug"] > max4 and Di[i]["id"][0:2] == "51":
        in4 = Di[i]["id"]
        name4 = Di[i]["name"]
        max4 = Di[i]["num_drug"]
    if Di[i]["num_drug"] > max5 and Di[i]["id"][0:2] == "54":
        in5 = Di[i]["id"]
        name5 = Di[i]["name"]
        max5 = Di[i]["num_drug"]

start_county_id = []
start_county_id.append(in1)
start_county_id.append(in2)
start_county_id.append(in3)
start_county_id.append(in4)
start_county_id.append(in5)
start_county_name = []
start_county_name.append(name1)
start_county_name.append(name2)
start_county_name.append(name3)
start_county_name.append(name4)
start_county_name.append(name5)
print(start_county_name)

workbook1 = xlrd.open_workbook('paint/11.xlsx')
booksheet1 = workbook1.sheet_by_name("Sheet2")
row_num = booksheet1.nrows
for ye in range(2018, 2030):
    result, index = regre(ye)

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('My Worksheet' + str(ye))
    name = "boom" + str(ye)
    locals()[name] = []
    in1 = in2 = in3 = in4 = in5 = ""
    name1 = name2 = name3 = name4 = name5 = ""
    max1 = max2 = max3 = max4 = max5 = 0
    for i in range(1, len(Di)):
        if Di[i]["num_drug"] > max1 and Di[i]["id"][0:2] == "21" and Di[i]["year"] == ye:
            in1 = Di[i]["id"]
            name1 = Di[i]["name"]
            max1 = Di[i]["num_drug"]
        if Di[i]["num_drug"] > max2 and Di[i]["id"][0:2] == "39" and Di[i]["year"] == ye:
            in2 = Di[i]["id"]
            name2 = Di[i]["name"]
            max2 = Di[i]["num_drug"]
        if Di[i]["num_drug"] > max3 and Di[i]["id"][0:2] == "42" and Di[i]["year"] == ye:
            in3 = Di[i]["id"]
            name3 = Di[i]["name"]
            max3 = Di[i]["num_drug"]
        if Di[i]["num_drug"] > max4 and Di[i]["id"][0:2] == "51" and Di[i]["year"] == ye:
            in4 = Di[i]["id"]
            name4 = Di[i]["name"]
            max4 = Di[i]["num_drug"]
        if Di[i]["num_drug"] > max5 and Di[i]["id"][0:2] == "54" and Di[i]["year"] == ye:
            in5 = Di[i]["id"]
            name5 = Di[i]["name"]
            max5 = Di[i]["num_drug"]
    print(max1, max2, max3, max4, max5)
    locals()[name].append(in1)
    locals()[name].append(in2)
    locals()[name].append(in3)
    locals()[name].append(in4)
    locals()[name].append(in5)
    del in1, in2, in3, in4, in5
    print(locals()[name])

    for i in range(num_county):
        index_obj = ""
        for j in range(1, row_num):
            row = booksheet1.row_values(j)
            inti = int(row[5])
            if str(inti) == county[i]:
                inti = int(row[0])
                index_obj = str(inti)
                break
        worksheet.write(i, 0, label=index_obj)
        worksheet.write(i, 1, label=result[i])
    workbook.save('paint/Excel_Workbook' + str(ye) + '.xls')

