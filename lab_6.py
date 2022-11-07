import random

print("Введите количество узлов")
N = int(input())
max_graph = ((N ** 2) - N) // 2
print("Введите число рёбер от", N - 1, "до", max_graph)
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

for x in range(N):  # Очистка матрицы от лишних значений -1.
    for y in range(N):
        if graph[x][y] == -1:
            graph[x][y] = 0

for row in graph:  # Вывод матрицы.
    print(row)

print('\n\n\n')

for k in range(N):  # Алгоритм Флойда-Уоршелла
    for i in range(N):
        for j in range(N):
            # if i == j:
            #     continue
            if graph[i][j] == 0:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in graph:  # Вывод матрицы.
    print(row)