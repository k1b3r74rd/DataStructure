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

        if self.start_node.item == x: # Если элемент - первый в списке.
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

    # def clear_list(self, data):
    #     data.clear()
    #     print('Список очищен: ', data)


if __name__ == "__main__":
    new_list = List()
    for i in range(15):
        a = random.randint(-50, 50)
        new_list.insert_at_end(a)

    new_list.traverse_list()

    delet = int(input())

    new_list.delete_element_by_value(delet)
    new_list.traverse_list()
    # new_list.clear_list(new_list)
