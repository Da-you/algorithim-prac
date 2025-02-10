# 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다. 즉 약수가 1과 자기 자신뿐이며 1보다 큰 자연수!

# 기존의 함수에서는 2~19 까지 모든 수를 한번씩 다 나누었지만 2와 3으로 나눠 떨어지지 않는다면 2*3 인 6도 당연히 떨어지지 않는다.
input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
