input = "abcba"


def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    is_palindrome(string[1:-1])
    return True


print(is_palindrome(input))
