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
        print('.')

plt.title('plotting')
plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='asc')
plt.plot([1, 2, 3, 4], [12, 43, 25, 45], color='g', linestyle=':', label='zigzag')
plt.plot([40, 30, 20, 10, 0], 'b.', label='desc')
plt.legend()
plt.show()

f.close()

print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은', max_data + '로, ', max_temp, '도 였습니다.')