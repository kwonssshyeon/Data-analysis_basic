import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)
result = []
high = []
low = []

for row in data:
    if row[-1] != '' and row[-2] != '':
        if 1983 <= int(row[0].split('-')[0]):
            if row[0].split('-')[1] == '09' and row[0].split('-')[2] == '15':
                high.append(float(row[-1]))
                low.append(float(row[-2]))

plt.figure(figsize=(10, 2))
plt.rc('font', family='Malgun Gothic')
plt.title('내 생일(9/15) 기온변화')

plt.plot(high, 'r', label='high')
plt.plot(low, 'b', label='low')
plt.legend(loc=1)

plt.show()


