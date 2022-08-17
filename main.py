import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='cp949')

max_temp = -999
max_data = ''
i = 0

data = csv.reader(f, delimiter=',')
header = next(data)
for row in data:
    if row[-1] == '':
        row[-1] = -999
    row[-1] = float(row[-1])

    if max_temp < row[-1]:
        max_data = row[0];
        max_temp = row[-1]

    if i < 10:
        i += 1
        print(row)
    elif i < 20:
        i += 1
        print(' .')

f.close()

print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은', max_data + '로, ', max_temp, '도 였습니다.')

plt.plot([10,20,30,40])
plt.show()