# Требуется вычислить, сколько раз встречается некоторое число X в 
# списке A[1..N]. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых 
# чисел Ai. Последняя строка содержит число X

list_range = int (input("введите размер списка: "))
numofelement = 1
list = []
for _ in range(list_range):
    list_element = int(input(f"введите элемент {numofelement}: "))
    list.append(list_element)
    numofelement += 1
search_num = int (input("введите число, которое нужно найти: "))
print(list)
print(list.count(search_num))