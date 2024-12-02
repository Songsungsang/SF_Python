vending_machine = ['게토레이', '레쓰비', '생수', '이프로']

drink = input("마시고 싶은 음료? ")

if drink in vending_machine :
    print(f"{drink} 드릴게요")
else :
    print(f"{drink}는 지금 없네요")