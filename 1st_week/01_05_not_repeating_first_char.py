# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오

def find_alphabet(string):
    occurrence_array = [0] * 26

    for char in string:
        arr_index = ord(char) - ord('a')
        occurrence_array[arr_index] += 1
    return occurrence_array


input = "abadabac"


def find_not_repeating_first_character(string):
    # string에서 빈도 수가 1인 알파벳을 찾는다.
    # 해당 알파벳에서 처음 나온 알파벳을 찾는다.

    occurrence_array = find_alphabet(string)

    not_repeating_char_array = []
    for index in range(len(occurrence_array)):
        alphabet_occurrence = occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_char_array.append(chr(index + ord("a")))
    for char in string:
        if char in not_repeating_char_array:
            return char
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
