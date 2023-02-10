# исходный списос списков
inList = [[10, 20, 30], [40, 50, 60],
          [70, 80, 90], [100, 110, 120]]
outList = []
# задаем кол-во списков в новом массиве
for i in range(len(inList[0])):
    outList.append([])
    # задаем кол-во элементов в каждом списке
    for j in range(len(inList)):
        outList[i].append(inList[j][i])
print(outList)

# по сути, мы выполнили обычное траспонирование матрицы
# если быть знакомым с numpy то решить можно так:
import numpy as np

arr = np.array(inList)
print(arr.T)

