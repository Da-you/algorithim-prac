class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first_node = Node(3)
print(first_node.data, first_node.next)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결하는 메서드
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(5)
print(linked_list.head.data)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()
