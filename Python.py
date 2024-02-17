from tokenize import Double
import math 

# <summary> Задание 1 Среднее арифметическое цифр дробной части числа </summary>
# <param name="x"> Число Х </param>
# <returns> Среднее арифметическое </returns>
def ArithmeticMean(x : Double):
    #...
    if x % 1 != 0:
        x = int(str(x).split('.')[1])
        n = len(str(x))
        counter = 0
        for i in range(n):
            counter += x % 10
            x = round((x / 10) - ((x % 10) / 10))
        return (counter / n)
    else: return 0
    # return round((x / 10) - ((x % 10) / 10))

# Задание 2 ПО для вендингового аппарата </summary>
# <param name="orderSum"> Сумма заказа (Integer / Целочисленный) </param>
# <param name="clientSum"> Внесенная сумма клиентом (Integer / Целочисленный) </param>
# <returns> Сдача формата номинал : количество (Dictionary / Словарь)</returns>
def Vending(orderSum : int, clientSum : int):
#...
    mas = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]
    x = clientSum - orderSum
    dict = {}
    for i in range(len(mas)):
        if x >= mas[i]:
            to_dict = x // mas[i]
            dict[mas[i]] = to_dict
            x = x - (x // mas[i]) * mas[i]
    return dict

# <summary> Задание 3 Заказы на линзы для Инопланетян </summary>
# <param name="dioptries"> Значения диоптрий каждого Инопланетянина (Array / Массив) </param>
# <returns> Количество пар линз (Integer / Целочисленный) </returns>
def Lenses(dioptries : list):
    #...
    dioptries.sort()
    counter = 0
    length = len(dioptries) 
    i = 0
    while i+1 < length:
        if  dioptries[i+1] == dioptries[i] or dioptries[i+1] == dioptries[i]+1 or dioptries[i+1] == dioptries[i]+2:
            counter += 1
            i += 1
        else: counter += 1 
        i += 1
    if len(dioptries) % 2 != 0:
        counter += 1
    return counter
    
print(ArithmeticMean(10.12345))
print(Vending(41, 88))
print(Lenses([0, -3, -4, 0]))
