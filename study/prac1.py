print("문자열")

상호명 = "이자카야"
나이 = 31

print("우리 가게 업종은 " + 상호명 + "이야")
print("내 나이는 :", 나이, "입니다.")
# ㅁㅇㅁ 주석

메뉴1 = "꼬치1"
메뉴2 = "꼬치2"
메뉴3 = "꼬치3"
메뉴4 = "꼬치4"
메뉴5 = "꼬치5"
메뉴6 = "꼬치6"
메뉴7 = "꼬치7"
메뉴8 = "꼬치8"
메뉴9 = "꼬치9"

메뉴판 = ["꼬치1", "사과", "배", "토마토", "바나나", "꼬치2"]
menus = ["꼬치1", 2, 3, "토마토", 5, "꼬치2"]  # 자료형이 달라도 가능
print(메뉴판)
print(menus[1])

# for 변수 in 반복 범위:
#     반복 수행 문장
# 반복 범위는 range(100) 처럼 지정 가능
for menu in range(100):
    # 반복 범위에 존재하는 숫자를 menu 라는 변수에 담아 출력
    print(menu, "배고파")

for menu in menus:
    print(menu, "배고파")

# 조건문
# if 조건:
#     수행 행동
n = 70
if n >= 70:
    print("C")

키 = 50


# 함수
# def 함수명(입력값):
#     처리
#     return 출력
def validHight(키):
    제한통과여부 = 키 <= 220 and 키 >= 100
    출입금지 = 키 == 50
    if 제한통과여부:
        return print("탑승 가능")
    elif 출입금지:
        return print("탑승 불가")
    else:
        return print("미확인")


print("-------------------------")
validHight(키)


# 첫 번째 손님
# 나이 = 28
# 성인여부 = 나이 > 19
# if 성인여부:
#     print("성인입니다. 어서오세요!")
# else:
#     print("죄송합니다. 미성년자는 입장할 수 없습니다.")
#
# # 두 번째 손님
# 다음손님나이 = 18
# 성인여부 = 다음손님나이 > 19
# if 성인여부:
#     print("성인입니다. 어서오세요!")
# else:
#     print("죄송합니다. 미성년자는 입장할 수 없습니다.")
#
# # 세 번째 손님
# 다다음손님나이 = 48
# 성인여부 = 다다음손님나이 > 19
# if 성인여부:
#     print("성인입니다. 어서오세요!")
# else:
#     print("죄송합니다. 미성년자는 입장할 수 없습니다.")


def 성인_확인(나이):
    if 나이 >= 20:
        print("성인입니다. 어서오세요!")
    else:
        print("죄송합니다. 미성년자는 입장할 수 없습니다.")

성인_확인(28)
성인_확인(19)
