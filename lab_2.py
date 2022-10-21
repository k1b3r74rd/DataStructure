import random
import datetime

"""
Изучение алгоритмической сложности выбранных сортировок.
Задание 1: засечь время выполнения и количество операций сортировки для массивов с определенным кол-вом элементов.
Задание 2: засечь время выполнения и количество операций худшего и лучшего вариантов сортировки.
"""
# Генерация массивов для первого задания.
arrays = []
b = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 250, 300, 400, 500, 600, 800, 1000]
for elem in b:
    mas = []
    count_mas = 0
    for l in range(elem):
        count_mas += 1
        x1 = random.randint(1, 100000)
        mas.append(x1)
        if count_mas == elem:
            arrays.append(mas)

# Генерация массивов для второго задания.
arr1, arr2 = [], []
arrays2 = [arr1, arr2]
for i in range(1, 101):
    arr1.append(i)
for j in range(100, 0, -1):
    arr2.append(j)


def comb(data):
    """
    Сортировка расчёской.
    """
    count_comb = 0
    gap = len(data)
    swaps = True
    while gap > 1 or swaps:
        # count_comb += 1
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(data) - gap):
            j = i + gap
            if data[i] > data[j]:
                count_comb += 1
                data[i], data[j] = data[j], data[i]
                swaps = True
            else:
                count_comb += 1
    print(count_comb, end=' ')
    return data


def quick(data):
    """
    Быстрая сортировка. Для вычисления количества операций прибегнуть к Excel.
    """
    less = []
    pivotList = []
    more = []
    c=0
    if len(data) <= 1:
        c+=1
        return data
    else:
        pivot = data[0]
        c+=1
        for i in data:
            if i < pivot:
                less.append(i)
                c+=1
            elif i > pivot:
                more.append(i)
                c+=1
            else:
                pivotList.append(i)
                c+=1
        less = quick(less)
        more = quick(more)
        print(c, end=' ')
        return less + pivotList + more


def bubble(data):
    """
    Сортировка обменом/пузырьком.
    """
    count_bubble = 0
    for i in range(0, len(data) - 1):
        count_bubble += 1
        for j in range(i+1, len(data) - 1):
            count_bubble += 1
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                count_bubble += 1
    print(count_bubble, end=' ')
    return data


def timedelta(func):
    """
    Вычисление затраченного времени.
    """
    for elem in arrays2:
        a = datetime.datetime.now()
        func(elem)
        b = datetime.datetime.now()
        c = b - a
        print(len(elem), c)
    print('\n\n')


if __name__ == '__main__':
    # При запуске функции, остальные комментировать. Для каждого задания в def timedelta менять используемые массивы.
    timedelta(comb)
    # timedelta(quick)
    # timedelta(bubble)
