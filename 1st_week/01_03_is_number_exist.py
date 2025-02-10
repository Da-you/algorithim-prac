# Q. 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환하시오.

def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    # 주어진 배열을 순회해 주어진 number 의 값을 찾아 boolean 값을 출력
    for n in array:  # array 길이만큼 아래 연산 실행
        if n == number:  # 비교 연산 1번 실행
            return True

    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3, 5, 6, 1, 2, 4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6, 6, 6]))
print("정답 = True 현재 풀이 값 =", result(2, [6, 9, 2, 7, 1888]))
