"""
E. Список дел

Васе нужно распечатать свой список дел на сегодня. Помогите ему: напишите
функцию, которая печатает все его дела. Известно, что дел у Васи не больше
5
0
0
0
.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать
только функцию, которая принимает на вход голову списка и печатает его
элементы. Ниже дано описание структуры, которая задаёт вершину списка.
Внимание! Решение надо отправлять только в виде файла с расширением, которое
соответствует вашему языку. Иначе даже корректно написанное решение не пройдет
тесты.

Формат ввода
В качестве ответа сдайте только код функции, которая печатает элементы списка.
Python:
Если вы пишете на Python, функция должна называться solution и принимать на
вход вершину node.
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
void solution(Node* head);
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
Файл должен содержать public class Solution с public static void
solution(Node<String> head)

class Node<V> {
    public V value;
    public Node<V> next;

    public Node(V value, Node<V> next) {
        this.value = value;
        this.next = next;
    }
}
Формат вывода
Функция должна напечатать элементы списка по одному в строке.
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


def solution(node):
    while node:
        print(node)
        node = node.next_item


n3 = Node('third')
n2 = Node('second', n3)
n1 = Node('first', n2)

solution(n1)
