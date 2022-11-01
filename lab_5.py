class Node:
    def __init__(self, key=None):
        """
        Связь в дереве.
        """
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        """
        Объявление дерева.
        """
        self.root = None

    def insert(self, node):
        """
        Вставка элемента в дерево.
        По принципу: если элемент меньше корня - то влево, иначе вправо
        """
        if self.root is None:
            self.root = Node(node)
            return

        current = self.root
        while True:
            if node < current.key:
                if current.left is None:
                    current.left = Node(node)
                    break
                current = current.left
            elif node > current.key:
                if current.right is None:
                    current.right = Node(node)
                    break
                current = current.right
            else:
                print(f"Key {node} already exists")
                break

    def tree_height(self):
        """
        Метод подсчёта высоты дерева (через рекурсию).
        """

        def height(node):
            if node is None:
                return 0

            lheight = height(node.left)
            rheight = height(node.right)

            return max(lheight, rheight) + 1

        depth = height(self.root)
        print(depth)

    def breadth_tree(self):
        """
        Обход/вывод дерева в ширину.
        """
        lst = []

        def traverse(node, depth):
            if node.left is not None:
                lst.append(node.left)
            if node.right is not None:
                lst.append(node.right)
            if depth > (len(lst) - 2):
                return
            else:
                traverse(lst[depth + 1], depth + 1)

        lst.append(self.root)
        if self.root is None:
            print('Дерево пустое')
            return
        traverse(self.root, 0)

        # Результат обхода существует в lst таблице
        for node in lst:
            print(node.key, end=' ')

        print('\n', end='')

        for node in lst:
            type_check = lambda x: x.key if x is not None else x
            print(node.key, type_check(node.left), type_check(node.right))

    def delete_element(self, x):
        """
        Удаление элемента из дерева.
        """
        def replace_child(parent, old, new):
            if parent is None:
                tree.root = new
            elif parent.left == old:
                parent.left = new
            elif parent.right == old:
                parent.right = new

        parent = None
        v = tree.root

        while True:
            if v is None:
                return
            if x < v.key:
                parent = v
                v = v.left
            elif x > v.key:
                parent = v
                v = v.right
            else:  # x == v.key
                break

        result = None

        if v.left is None:
            result = v.right
        elif v.right is None:
            result = v.left
        else:
            min_node_parent = v
            min_node = v.right
            while min_node.left is not None:
                min_node_parent = min_node
                min_node = min_node.left

            result = v
            v.key = min_node.key
            replace_child(min_node_parent, min_node, min_node.right)

        replace_child(parent, v, result)

    def clear_tree(self):
        """
        Удаление дерева.
        """
        self.root = None


if __name__ == '__main__':
    import random

    tree = Tree()
    print('2. Заполнение дерева + проверка на повтор элемента:')
    for i in range(random.randint(7, 11)):
        tree.insert(random.randint(1, 50))

    print('\n5. Вывод дерева + узлы:')
    tree.breadth_tree()
        
    print('\n3. Удаление элемента из дерева: \nВведите элемент >> ', end='')
    elem_to_delete = int(input())
    tree.delete_element(elem_to_delete)

    tree.breadth_tree()

    print('\n6. Вычисление высоты дерева: ')
    tree.tree_height()

    print('\n4. Удаление дерева:')
    tree.clear_tree()
    tree.breadth_tree()
