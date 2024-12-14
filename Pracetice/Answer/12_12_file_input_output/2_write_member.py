name_input = input("이름을 입력하세요. ")
password_input = input("비밀번호를 입력하세요. ")

with open("./Answer/12_12/member.txt", "r") as f:
    success = False
    for i in range(3):
        member = f.readline().split()
        if member[0] == name_input and member[1] == password_input: #현재 라인의 이름이 name_input과 같고 비밀번호도 맞다면
            print("로그인 성공")
            success = True
            break

if success == False:
    print("로그인 실패")

