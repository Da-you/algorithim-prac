finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    array.sort()
    min_idx = 0
    max_idx = len(array) -1
    guess_idx =  (min_idx + max_idx) // 2

    while min_idx <= max_idx:
        if array[guess_idx] == target:
            return True
        elif array[guess_idx] < target:
            min_idx = guess_idx + 1
        else: # array[guess_idx] > target:
            max_idx = guess_idx - 1
        guess_idx =  (min_idx + max_idx) // 2
    # 이 부분을 채워보세요!
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)