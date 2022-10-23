import random


class Node:
    def __init__(self, data):
        """
        Узел списка.
        """
        self.item = data
        self.nref = None
        self.pref = None


class List:
    def __init__(self):
        """
        Инициализация списка.
        """
        self.start_node = None

    def insert_at_end(self, data):
        """
        Заполнение списка (добавление элементов в конец).
        """
        if self.start_node is None:  # Если список пуст...
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:  # Если не пуст...
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def traverse_list(self):
        """
        Прогонка списка.
        """
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, end=' ')
                n = n.nref
            print()

    def delete_element_by_value(self, x):
        """
        Удаление элемента из списка.
        """
        if self.start_node is None:
            print("Список пуст.")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Значение не найдено.")
            return

        if self.start_node.item == x:  # Если элемент - первый в списке.
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            print('Элемент удален (первый в списке).')
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:  # Если элемент НЕ последний в списке.
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:   # Если элемент - последний в списке.
            if n.item == x:
                n.pref.nref = None
            else:
                print("Элемент не найден.")

    def clear_list(self):
        """
        Аннигиляция списка.
        """
        while self.start_node is not None:
            if self.start_node.nref is None:
                self.start_node = None
                return
            self.start_node = self.start_node.nref

    def find_element(self, elem):
        """
        Поиск элемента в списке через прогонку списка.
        """
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            id = 0
            element_is_found = False
            while n is not None:
                if n.item == elem:
                    element_is_found = True
                    break
                else:
                    id += 1
                    n = n.nref

            if element_is_found:
                print(f'Айди элемента: {id}')
            else:
                print('Элемент не найден.')

    def sortList(self):
        if self.start_node is None:
            return
        else:
            current = self.start_node
            while current.nref is not None:
                index = current.nref
                while index is not None:
                    if current.item > index.item:
                        current.item, index.item = index.item, current.item
                    index = index.nref
                current = current.nref

    def concat_lists(self, extra):
        elem = extra.start_node
        while elem is not None:
            self.insert_at_end(elem.item)
            elem = elem.nref


if __name__ == "__main__":
    # Инициализация и генерация списка из рандомных 20 значений от -50 до 50.
    main_list = List()
    extra_list = List()
    print('1. Сгенерированный список: ')
    for i in range(19):
        a,b = random.randint(-50, 50), random.randint(-50, 50)
        main_list.insert_at_end(a)  # Вставка элемента в конец
        extra_list.insert_at_end(b)  # Список для задания по варианту
    main_list.traverse_list()  # Вывод списка

    print('2. Введите число, которое необходимо вставить в конец списка: ', end='')
    insert_elem = int(input())
    main_list.insert_at_end(insert_elem)
    print('Обновленный список: ')
    main_list.traverse_list()

    print('3. Введите число, которое необходимо удалить из списка: ', end='')
    delete_element = int(input())
    main_list.delete_element_by_value(delete_element)
    print('Обновленный список: ')
    main_list.traverse_list()

    print('4. Введите число, которое необходимо найти в списке: ', end='')
    element_to_find = int(input())
    main_list.find_element(element_to_find)

    print('5. Сортивка и слияние двух двусвязных списков: ')
    print('Изначальные списки: ')
    main_list.traverse_list()
    extra_list.traverse_list()
    print('Отсортированные списки: ')
    main_list.sortList()
    main_list.traverse_list()
    extra_list.sortList()
    extra_list.traverse_list()
    print('Слияние списков: ')
    main_list.concat_lists(extra_list)
    main_list.traverse_list()
    print('Финальный результат: ')
    main_list.sortList()
    main_list.traverse_list()

    print('6. Очистка списка: ')
    main_list.clear_list()
    main_list.traverse_list()

