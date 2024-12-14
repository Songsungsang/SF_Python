name = input("이름을 입력하세요. ")
password = input("비밀번호를 입력하세요. ")

dictUser = dict()
with open("./Answer/12_12/member.txt", "r") as f:
    for line in f:
        n, p = line.split()
        dictUser[n] = p
    print(dictUser)

    if password == dictUser.get(name): #입력된 비밀번호가 이름이 가리키는 비밀번호와 일치할경우
    # if dic[name] == password:
        word = "로그인 성공!"
    else:
        word = "로그인 실패!"
    
    print(word)

"""
if word == "로그인 성공!":
    phone_number = input("전화번호를 입력하세요. ")
    dictPhone = dict()
    with open("./Answer/12_12/member_tel.txt", "r+") as f:
        strf = f.read() #전체를 담은 스트링
        f.seek(0) # 처음으로 다시 돌아가기
        for line in f: # 각 라인마다 사용자와 전화번호
            n, p = line.split()
            dictPhone[n] = p
        print(dictUser)

        getName = dictPhone.get(name) # 사용자 이름으로 전화번호가 있는지
        print(getName)
        if getName is None: #없다면
            f.write(f"{name} {phone_number}\n") #그대로 쓰기
        else: # 있다면
            f.seek(strf.find(name)) #이름의 위치 찾아서
            f.write(f"{name} {phone_number}\n")
"""
#정답 코드
if word == "로그인 성공!":
    phone = input("전화번호를 입력하세요. ")
    user_tel = name + " " + phone + "\n"
    with open("./Answer/12_12/member_tel.txt", "r+") as f:
         m_tel_list = f.readlines()
    print(m_tel_list)

with open("member_tel.txt", "w") as f:
    write = False
    for i in m_tel_list:
        if i.split()[0] == name:
            f.write(user_tel)
            write = True
        else :
            f.write(i)
    if not write:
        print("not write", user_tel)
        f.write(user_tel)