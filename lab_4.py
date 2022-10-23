class Stack:  # LIFO
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def push(self, elem):
        self.stack.append(elem)

    def size(self):
        return len(self.stack)

    def upper_elem(self):
        return self.stack[len(self.stack)-1]


class Queue:  # FIFO
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def pop(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def push(self, elem):
        self.queue.append(elem)

    def first_elem(self):
        return self.queue[0]


if __name__ == "__main__":
    from random import randint

    stack = Stack()
    queue = Queue()
    for i in range(10):
        a, b = randint(-50, 50), randint(-50, 50)
        stack.push(a)
        queue.push(b)

    print('Работа со стеком:', stack.stack)
    print('1. Удаление из стека:')
    print(stack.pop(), '\nОбновленный стек:', stack.stack)

    print('2. Добавление в стек. Введите целое число: >>> ', end='')
    add1 = int(input())
    stack.push(add1)
    print("Обновленный стек:", stack.stack)

    print('3. Число элементов в стеке:', stack.size())
    print('4. Верхний элемент стека:', stack.upper_elem())
    print('Стек:', stack.stack)

    print('\n')

    print('Работа с очередью:', queue.queue)
    print('1. Число элементов в очереди:', queue.size())

    print('2. Удалить из очереди:')
    queue.pop()
    print('Обновленная очередь:', queue.queue)

    print('3. Добавить в очередь. Введите целое число: >>> ', end='')
    add2 = int(input())
    queue.push(add2)
    print('Обновленная очередь:', queue.queue)

    print('4. Получить первый элемент:', queue.first_elem())
    print('Очередь:', queue.queue)
