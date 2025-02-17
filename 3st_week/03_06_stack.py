class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 어떻게 하면 될까요?
        new_head = Node(value)  # ex 기존의 [4] 노드만 있는 상태에서 [3] 노드를 생성
        new_head.next = self.head  # [3] -> [4]
        self.head = new_head  # [3] 노드를 현재 헤드로 지정

    # pop 기능 구현
    def pop(self):
        # 어떻게 하면 될까요?
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        # 어떻게 하면 될까요?
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None


stack = Stack()
stack.push(4)
print(stack)

print(stack.peek())

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

stack.pop() # [5] 노드 제거
print(stack.peek()) # [3] 노드 반환