with open("./Answer/12_12/member.txt", "w") as f:
    for i in range(3):
        text = input("회원 이름과 비밀번호를 입력해 주세요(예: 홍길동 1111) : ")
        f.write(text + "\n")

with open("./Answer/12_12/member.txt", "r") as f:
    for i in range(3):
        text = f.readline().split()
        print(f"회원 이름: {text[0]}\n회원 비밀번호: {text[1]}")
