# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.
# (단 최빈값을 가진 알파벳이 여러개일 경우 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오)

# 문자인지 확인하는 메서드
# print("a".isalpha())    # True
# print("1".isalpha())    # False
#
# s = "abcdefg"
# print(s[0].isalpha())   # True

# 내장 함수 ord() 이용해서 아스키 값 받기
# print(ord('a'))               # 97
# print(ord('a') - ord('a'))    # 97-97 -> 0
# print(ord('b') - ord('a'))    # 98-97 -> 1
# 아스키 값 -> 문자
# chr(97) -> 'a'

def find_max_occurred_alphabet(string):
    # alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    #                   "t", "u", "v", "x", "y", "z"]
    # max_occurrence = 0
    # max_alphabet = alphabet_array[0]
    # for alphabet in alphabet_array: # 알파벳을 순회하며 몇 번 나왔는지 확인
    #     occurrence = 0
    #     for char in string: # 문자열의 글자가 현재 알파벳과 일치한다면 빈도수 +1
    #         if char == alphabet:
    #             occurrence += 1
    #     if occurrence > max_occurrence: # 해당 알파벳의 빈도 수가 지정한 횟수보다 많다면 그 알파벳을 가장 자주나온 알파벳으로 저장
    #         max_alphabet = alphabet
    #         max_occurrence = occurrence
    # return max_alphabet

    # 각 알파벳의 빈도수를 alphabet_occurrence_array에 저장, 문자열을 순회해 문자가 알파벳인지 확인, 알파벳을 아스키 값으로 인덱스화해 알파벳의 빈도수를 업데이트
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
