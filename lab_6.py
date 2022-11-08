import random

print("Введите количество узлов: >>>", end=' ')
N = int(input())
max_graph = ((N ** 2) - N) // 2
print("Введите число рёбер от", N - 1, "до", max_graph, ': >>>', end=' ')
M = int(input())

graph = [[0] * N for i in range(N)]  # Создание матрицы дорог и заполнение главной диагонали
for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0
        else:
            graph[i][j] = -1

l = 0
while True:  # Заполнение матрицы значениями дорог.
    irand = (random.randint(1, 1000000)) % N
    jrand = (random.randint(1, 1000000)) % N
    if graph[irand][jrand] == -1:
        x1 = random.randint(1, 35)
        graph[irand][jrand] = x1
        graph[jrand][irand] = x1
        l += 1
        if l == M:
            break
    else:
        continue

print('Сгенерированный граф: ')
for row in graph:  # Вывод матрицы.
    print(row)

for k in range(N):  # Меняем -1 на "объездной путь"
    for i in range(N):
        for j in range(N):
            if graph[i][j] == -1:
                graph[i][j] = graph[i][k] + graph[k][j]

print('\nОтредактированный граф: ')
for row in graph:  # Вывод матрицы.
    print(row)

print('Введите длину дороги: >>>', end=' ')
option_task = int(input())
route_is_available = False
for i in range(N):
    city_count = 0
    for j in range(N):
        if graph[i][j] <= option_task:
            city_count += 1

    if city_count == N:
        route_is_available = True
        break

if route_is_available:
    print('Такой город ЕСТЬ.')
else:
    print('Таких городов НЕТ.')