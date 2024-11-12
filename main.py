import random #подключение библиотеки рандом

nums=[random.randint(-50, 50) for _ in range(25)] #инициализация списка значений от -50 до 50

pos_num=0
neg_num=0
nul_num=0
#инициалзация переменных для подсчитывания кол-ва совпадений
for num in nums:
    if num>0:#увеличение счетчика положительных
        pos_num+=1
    if num<0:#увеличение счетчика отрицательных
        neg_num+=1
    if num==0:#подсчет кол-ва 0
        nul_num+=1

kolv_num=len(nums)#количество цифр через длинну списка
pos_proc=(pos_num/kolv_num)*100#подсчет процента положительных значений
neg_proc=(neg_num/kolv_num)*100#подсчет процента отрицательных значений
nul_proc=(nul_num/kolv_num)*100#подсчет процента нулей

max_num=max(nums)#инициализация переменной с максимальным значением списка
min_num=min(nums)#инициалхиация переменной с минимальным значением списка

print(f"Список чисел: \n{nums}")
print("\nРезультаты")
print(f"Кол-во положительных: {pos_num}\nПроцент положительных: {pos_proc}%")
print(f"Кол-во отрицательных: {neg_num}\nПроцент отрицательных: {neg_proc}%")
print(f"Кол-во нулей: {nul_num}\nПроцент нулей: {nul_proc}%")
print(f"Максимальное значение: {max_num}")
print(f"Минимальное значение: {min_num}")
#вывод итоговых значений переменных
