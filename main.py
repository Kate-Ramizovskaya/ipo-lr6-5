import random

nums=[random.randint(-50, 50) for _ in range(25)]

pos_num=0
neg_num=0
nul_num=0

for num in nums:
    if num>0:
        pos_num+=1
    if num<0:
        neg_num+=1
    if num==1:
        nul_num+=1

kolv_num=len(nums)
pos_proc=(pos_num/kolv_num)*100
neg_proc=(neg_num/kolv_num)*100
nul_proc=(nul_num/kolv_num)*100

max_num=max(nums)
min_num=min(nums)

print(f"Список чисел: \n{nums}")
print("\nРезультаты")
print(f"Кол-во положительных: {pos_num}\nПроцент положительных: {pos_proc}%")
print(f"Кол-во отрицательных: {neg_num}\nПроцент отрицательных: {neg_proc}%")
print(f"Кол-во нулей: {nul_num}\nПроцент нулей: {nul_proc}%")
print(f"Максимальное значение: {max_num}")
print(f"Минимальное значение: {min_num}")
