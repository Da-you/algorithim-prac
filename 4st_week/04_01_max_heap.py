class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 전체 배열에 값을 추가, append 함수로 추가 그러면 추가된 원소의 인덱스는 len(self.items) - 1
    # 해당 원소의 인덱스 len(self.items) -1 부터 시작
    # 추가된 인덱스 와 부모 노드의 인덱스 노드 값을 비교 (비교는 cur_idx 가 제일 꼭대기 칸, 1이 되기 전까지 반복)
    # 만약 자식 노드의 값이 더 크다면 cur_idx 에 parent_idx를 넣는다.
    def insert(self, value):
        self.items.append(value)
        cur_idx = len(self.items) - 1
        while cur_idx > 1:
            parent_idx = cur_idx // 2
            if self.items[parent_idx] < self.items[cur_idx]:
                self.items[parent_idx], self.items[cur_idx] = self.items[cur_idx], self.items[parent_idx]
                cur_idx = parent_idx
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
