# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다. 즉 약수가 1과 자기 자신뿐이며 1보다 큰 자연수!

input = 20


def find_prime_list_under_number(number):
    prime_list = []
    # 2 ~ 20 까지 찾기
    for n in range(2, number + 1):  # 2~n 까지의 숫자들이 n 에 들어가는 것을 반복한다.( 1보다 큰 자연수를 모음)
        #       해당 숫자가 소수라면 prime_list= [] 에 넣어라
        for i in range(2, n):  # 2 부터 n -1 까지를 i 에 들어가는 것을 반복 (n = 2,3,4,5,6,7, ~ 20, i = n-1)
            if n % i == 0:  # 소수가 아님
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
