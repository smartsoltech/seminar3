array = []
size = int(input('Введите количество элементов массива: '))
sum = 0
avg = 0
index = 0
for item in range(int(size)):
    array.append(input(f'Введите {item+1} элемент массива: '))
print(f'Массив заполнен: {array}')
while index < int(size):
    sum = int(sum)+int(array[index])
    index = index+1
avg = sum/size
print (f'Арифметическое среднее значение массива {array} равняется {avg}')