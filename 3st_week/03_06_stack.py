class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 현재 스택에 [4] 존재 , [3] 이 추가되면 [3] -> [4] 형태가 되어야 함
        new_head = Node(value)  # [3] 추가
        new_head.next = self.head  # 추가 노드 [3] 다음 데이터를 기존의 [4] 로 연결 즉 [3] -> [4] 형태를 만든
        self.head = new_head  # 현재 head 값을 [3] 으로 변경
        return

    # pop 기능 구현
    def pop(self):
        # [3] -> [4] 형태의 스택에서 Pop  실행시 [3] 이 반환되면서 빠져 [4] 만 존재하는 형태가 되어야 한다.
        # 링크드 리스트에서 현재 head 값 제거는 head를 다른 변수에 저장후 현재 노드를 다음 노드로 헤드를 변경
        # 만약 스택이 비어있다면 에러를 반환
        if self.is_empty():
            return "Stack is empty"

        pop_head = self.head
        self.head = self.head.next
        return pop_head

    def peek(self):
        # 제일 위에 있는 노드의 값을 반환
        # [3] -> [4] 형태의 스택에서 [3] 반환
        if self.is_empty():
            return "Stack is empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(4)

stack.push(3)
print(stack.peek()) # 3

stack.push(5)
print(stack.peek()) # 5

stack.pop() # 5 삭제
print(stack.peek()) # 3