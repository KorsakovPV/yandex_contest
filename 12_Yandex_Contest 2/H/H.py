"""
H. Все наоборот

Вася решил запутать маму —– делать дела в обратном порядке. Список его дел
теперь хранится в двусвязном списке. Напишите функцию, которая вернёт список в
обратном порядке.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
только функцию, которая принимает на вход голову двусвязного списка и
возвращает голову перевернутого списка. Ниже дано описание структуры, которая
задаёт вершину списка.
Внимание! Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение не пройдет
тесты.

Формат ввода
Функция принимает на вход единственный аргумент — голову двусвязного списка.
Python:
Если вы пишете на Python, функция должна называться solution и принимать на
вход вершину node.
Узел списка описывается следующим классом:

class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
С++:
struct Node {
    Node(const std::string &value, Node* next, Node* prev) : value(value),
    next(next), prev(prev) {}

    std::string value;
    Node* next;
    Node* prev;
};
Node* solution(Node* head);
Нужно подключить solution.h

Go:
type ListNode struct {
    data     string
    next  *ListNode
    prev  *ListNode
}
Ваша функция должна называться Solution.

JS:
class Node {
  constructor(value = null, next = null, prev = null) {
    this.value = value;
    this.next = next;
    this.prev = prev;
  }
}
Ваша функция должна называться solution.

Java:
Файл должен содержать public class Solution с public static Node<String>
solution(Node<String> head)

class Node<V> {
    public V value;
    public Node<V> next;
    public Node<V> prev;

    public Node(V value, Node<V> next, Node<V> prev) {
        this.value = value;
        this.next = next;
        this.prev = prev;
    }
}
Формат вывода
Функция должна вернуть голову развернутого списка.
Примечания
Решение нужно отправлять в виде файла с расширением соответствующем вашему
языку программирования. Нужно выбирать компилятор make. Для Java файл должен
называться Solution.java Для остальных языков программирования это имя
использовать нельзя (имя solution тоже).
"""


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value


def solution(node):
    while node:
        node.next, node.prev = node.prev, node.next
        if node.prev is None:
            return node
        node = node.prev


def solution_print_doble(node):
    while node:
        print(node)
        node = node.next


def solution_print(node):
    while node:
        print(node)
        node = node.next_item


def solution_del(node, index):
    head = node

    if index == 0:
        return node.next_item

    while index - 1:
        node = node.next_item
        index -= 1

    node.next_item = node.next_item.next_item
    return head


def solution_find(node, value):
    index = 0
    while node:
        if node.value == value:
            return index
        node = node.next_item
        index += 1
    return -1


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


head_DoubleConnected = DoubleConnectedNode('first')
node = head_DoubleConnected
for i in range(4):
    node_new = DoubleConnectedNode(str(i) * 5)
    node.next = node_new
    node_new.prev = node
    node = node.next

solution_print_doble(head_DoubleConnected)
print()
solution_print_doble(solution(head_DoubleConnected))

"""n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)
node_first = Node('first')
node = node_first
for i in range(4):
    node.next_item = Node(str(i)*5)
    node = node.next_item
solution_print(node_first)
print()
#solution_print(solution_del(node_first, 0))
print(solution_find(node_first, '333333'))"""
