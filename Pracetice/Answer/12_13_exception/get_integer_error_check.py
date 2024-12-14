is_int = False
while is_int == False :
    try :
        number = int(input("숫자 입력: "))
        is_int = True # except로 가지 않고 성공함
    except ValueError :
        print("정수가 아님! 정수를 입력하세요")

print(f"정수 입력 성공: {number}")