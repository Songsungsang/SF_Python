# 회원 찾기를 한번에 하기 위한 업그레이드 시도
name = input("이름을 입력하세요. ")
password = input("비밀번호를 입력하세요. ")

name_list = []
password_list = []
with open("./Answer/12_12/member.txt", "r") as f:
    success = False
    for i in range(3):
        member = f.readline().split()
        name_list.append(member[0])
        password_list.append(member[1])
    n_index = name_list.index(name)
    if password == password_list[n_index]:
        print("로그인 성공")
    else:
        print("로그인 실패")

"""
#dictionary를 만들어 한번에 답을 찾는 정답 코드
dictUser = dict()
with open("./Answer/12_12/member.txt", "r") as f:
    for line in f:
        n, p = line.split()
        dictUser[n] = p
    print(dic)

    if password == dictUser.get(name): #입력된 비밀번호가 이름이 가리키는 비밀번호와 일치할경우
    # if dic[name] == password:
        word = "로그인 성공!"
    else:
        word = "로그인 실패!"
    
    print(word)
"""
