"""
G. Заботливая мама

Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: напишите
функцию solution, определяющую индекс первого вхождения передаваемого ей на
вход значения в связном списке, если значение присутствует.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
только функцию, которая принимает на вход голову списка и искомый элемент, а
возвращает целое число — индекс найденного элемента или -1. Ниже дано описание
структуры, которая задаёт вершину списка.
Внимание! Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение не пройдет
тесты.

Формат ввода
Функция на вход принимает голову односвязного списка и элемент, который нужно
найти.
Python:
Если вы пишете на Python, функция должна называться solution и принимать на
вход вершину node и элемент, который надо найти.
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
int solution(Node *head, const std::string& elem);
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
Файл должен содержать public class Solution с public static int
solution(Node<String> head, String elem)

class Node<V> {
    public V value;
    public Node<V> next;

    public Node(V value, Node<V> next) {
        this.value = value;
        this.next = next;
    }
}
Формат вывода
Функция возвращает индекс первого вхождения искомого элемента в
список(индексация начинается с нуля). Если элемент не найден, нужно вернуть -1.
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


def solution_del(node, index):
    head = node

    if index == 0:
        return node.next_item

    while index - 1:
        node = node.next_item
        index -= 1

    node.next_item = node.next_item.next_item
    return head


def solution(node, value):
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
# solution_print(solution_del(node_first, 0))

print(solution(node_first, '333333'))
