vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로'] # 자판기
user_option = ['1', '소비자', '2', '주인']
task_option = ['1', '추가', '2', '삭제']

user = (input("사용자 종류를 입력하세요 : \n1. 소비자\n2. 주인\n"))

#if user != '1' and user != '소비자' and user != '2' and user != '주인':
if user not in user_option: #사용자 잘못 지정
    print("잘못된 사용자 종류입니다")
else:
    if user == '1' or user == '소비자': # 소비자 선택
        print(f"남은 음료수 : {vending_machine}")
        drink = input("마시고 싶은 음료? ")
        if drink in vending_machine : # 음료가 있다면
            print(f"{drink} 드릴게요")
            vending_machine.remove(drink) # pop 보다 remove를 쓰면 index 찾을 필요 없이 알아서 찾아줌
        else :
            print(f"{drink}는 지금 없네요")
    else:
        task = (input("할일 선택 : \n1. 추가\n2. 삭제\n")) # 주인 선택, 옵션 2개로 확장
        #if task != '1' and task != '추가' and task != '2' and task != '삭제':
        if task not in task_option : # 할일 잘못 지정
            print("잘못된 할일 선택입니다")
        elif task == '1' or task == '추가': # 음료 추가
            print(f"남은 음료수 : {vending_machine}")
            drink = input("추가할 음료수? ")
            vending_machine.append(drink)
            vending_machine.sort()
        elif task == '2' or task == '삭제': # 음료 삭제
            print(f"남은 음료수 : {vending_machine}")
            drink = input("삭제할 음료수? ")
            if drink in vending_machine: # 음료가 있다면
                vending_machine.remove(drink)
            else :
                print(f"{drink}는 지금 없네요")
    print(f"남은 음료수 : {vending_machine}")