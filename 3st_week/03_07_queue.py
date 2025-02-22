class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 현재 큐가 [4] -> [2]
        # [3] 추가 시 [4] -> [2] -> [3] 되어야 함
        add_node = Node(value)  # 추가할 노드를 생성
        if self.is_empty():  # 만약 큐가 비어 있다면 시작과 끝 지점을 추가 노드로 지정
            self.head = add_node
            self.tail = add_node
            return
        self.tail.next = add_node  # 현재 끝 지점의 다음 데이터를 추가한 add_node 로 지정
        self.tail = add_node  # 끝(tail) 지점을 추가된 노드로 변경

    def dequeue(self):
        # 큐의 데이터가 [3] -> [4] -> [5]
        # dequeue 실행 시 제일 앞의 데이터 [3] 이 빠져야 한다.
        # 즉, [4] -> [5] 되어야 함
        # 현재 head 값을 다른 변수에 저장 후 head가 지칭하는 노드를 현재 head 의 다음값으로 지정
        # 저장해둔 head 를 반환
        if self.is_empty():
            return "Queue is empty"
        delete_head = self.head  # 제거할 헤드를 별도의 변수로 저장
        self.head = self.head.next  # 현재 헤드를 다음 노드로 지정
        return delete_head.data  # 제거할 헤드의 데이터를 반환

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None
