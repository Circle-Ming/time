import numpy as np
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
print(array)


def regre(year):
    reg = []
    for iin in range(5):
        s = 0
        s1 = 0
        s2 = 0
        s_year = 0
        for jin in range(year - 2010):
            s += N10_17[jin][iin]
            s_year += jin
        avg_y = s / (year - 2010)
        avg_x = s_year / (year - 2010)
        for jin in range(year - 2010):
            s1 += (jin - avg_x) * (N10_17[jin][iin] - avg_y)
            s2 += (jin - avg_x) ** 2
        # b1 = (s1 - 8*13.5*avg_y)/(s2 - 8*(13.5**2))
        b1 = s1/s2
        b0 = avg_y - b1*avg_x
        y = b0 + b1*(year - 2010)
        reg.append(y)
    ma = reg[0]
    indx = 0
    for iin in range(5):
        if reg[iin] > ma:
            indx = iin
            ma = reg[iin]

    result = []
    for iin in range(5):
        if iin != indx:
            now = reg[iin] + array_state[indx, iin]*reg[indx]
            result.append(int(now))
        else:
            result.append(int(reg[iin]))
    print(result)
    N10_17.append(result)


regre(2018)
regre(2019)
regre(2020)
regre(2021)
