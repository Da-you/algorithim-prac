input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):  # 1: 0 ~ n - 1
        if string[i] != string[n - 1 - i]:  # i = 1  -> 1번 인덱스 3번 인덱스 비교( b ==b)
            return False
    return True


print(is_palindrome(input))
