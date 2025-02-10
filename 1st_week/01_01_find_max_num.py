# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.
def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0] # 배열의 첫 번째 값을 비교 값으로 지정
    for compare_num in array: # 배열을 순회해 아래 연산을 실행
        if compare_num > max_num: # 비교 값이 max_num 보다 높을 경우 비교 해당 값을 최대 값으로 변경
            max_num = compare_num
    print(max_num)
    return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))