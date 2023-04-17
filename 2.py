# Задача 18: Требуется найти в списке A[1..N] самый близкий по 
# величине элемент к заданному числу X. Пользователь в первой строке 
# вводит натуральное число N – количество элементов в списке. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

list_range = int(input("введите размер списка: "))
if list_range < 1: 
    print ("оазмер списка не может быть меньше 1")
else:
    count = 1
    list = []
    for _ in range(list_range):
        list_element = int(input(f"введите элемент массива {count}: "))
        list.append(list_element)
        count += 1
    element = int(input("введите число, с которым нужно сравнивать: "))
    index = 0
    minnum = abs(element - list[0])
    for i in range(list_range):
        searchingslement = abs(element - list[i])
        if searchingslement < minnum:
            minnum = searchingslement
            index = i
    print(f"самый близкий по величине элемент в списке = {list[index]}")