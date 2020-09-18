"""
F. Нелюбимое дело

Вася размышляет, что бы такое из списка не делать. Но, кажется, все пункты
очень важные! Вася решает загадать число и удалить дело, которое идёт под этим
номером. Список дел представлен в виде односвязного списка. Напишите функцию
solution, которая принимает на вход голову списка и номер удаляемого дела и
возвращает голову обновлённого списка.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
только функцию, которая принимает на вход голову списка и номер удаляемого
элемента и возвращает голову обновленного списка. Ниже дано описание структуры,
 которая задаёт вершину списка.
Внимание! Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение не пройдет
тесты.

Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить
(нумерация с нуля). Список содержит не более
5
0
0
0
 элементов.
Python:
Если вы пишете на Python, функция должна называться solution и принимать на
вход вершину node и номер удаляемого элемента.
Узел списка описывается следующим классом:

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item
С++:
struct Node {
    String value;
    Node* next;
    Node(const std::string &value, Node* next);
};
Node* solution(Node* head, int idx);
Нужно подключить solution.h

Go:
type ListNode struct {
    data   string
    next *ListNode
}
Ваша функция должна называться Solution.

JS:
class Node {
  constructor(value = null, next = null) {
    this.value = value;
    this.next = next;
  }
}
Ваша функция должна называться solution.

Java:
Файл должен содержать public class Solution с public static Node<String>
solution(Node<String> head, int idx)

class Node<V> {
    public V value;
    public Node<V> next;

    public Node(V value, Node<V> next) {
        this.value = value;
        this.next = next;
    }
}
Формат вывода
Верните голову списка, в котором удален нужный элемент.
Примечания
Решение нужно отправлять в виде файла с расширением соответствующем вашему
языку программирования. Нужно выбирать компилятор make.
Для Java файл должен называться Solution.java
Для остальных языков программирования это имя использовать нельзя (имя solution
 тоже).

"""


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution_print(node):
    while node:
        print(node)
        node = node.next_item


def solution(node, index):
    head = node

    if index == 0:
        return node.next_item

    while index - 1:
        node = node.next_item
        index -= 1

    node.next_item = node.next_item.next_item
    return head


def insert_node(node, index, value):
    head = node
    new_node = Node(value)
    if index == 0:
        new_node.next = node
        return new_node
    while index - 1:
        node = node.next
        index -= 1
    tmp = node.next
    node.next = new_node
    new_node.next = tmp
    return head


n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)

node_first = Node('first')
node = node_first

for i in range(4):
    node.next_item = Node(str(i) * 5)
    node = node.next_item

solution_print(node_first)
print()
solution_print(solution(node_first, 1))
