# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '✕' 혹은 '+' 연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.
# 단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.

def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    max_num = 0
    # 배열의 현재 값이 1 보다 낮거나 같으면 무조건 + 가 좋다 ( 1 * 2 = 2 , 1 + 2 = 3)
    for num in array: # N의 크기만 큼 아래 연산을 진행
        if num <= 1 or max_num <= 1: # 비교 연산
            max_num += num # 대입 연산
        else:
            max_num *= num # 대입 연산
    print(max_num)
    return max_num
# 시간 복잡도는 O(N)

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))