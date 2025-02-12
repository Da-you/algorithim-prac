finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 이진탐색은 O(log N)
def is_existing_target_number_binary(target, array):
    min_idx = 0
    max_idx = len(array) - 1
    guess_idx = (min_idx + max_idx) // 2  # // 는 내림을 의미 -> 25 // 2 == 12.5 가 아닌 12
    while min_idx <= max_idx:
        if array[guess_idx] == target:
            return True
        elif array[guess_idx] < target:
            min_idx = guess_idx + 1
        else: # array[guess_idx] > target:
            max_idx = guess_idx - 1
        guess_idx = (min_idx + max_idx) // 2
    # 구현해보세요!
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
