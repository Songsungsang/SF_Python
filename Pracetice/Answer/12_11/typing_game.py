import random
import time

word = ['황정민이', '좋아하는', '랜덤', '게임', '스타트', '아파트']

n = 1 # 1번 문제부터

input("타자게임이 준비되었을 경우 아무키 입력")
start = time.time() # 타이머 시작

while n < 11 :
    print("문제", n)
    question = random.choice(word) #word 중에 랜덤으로 추첨
    print(question)
    user = input()
    if question == user : # 문제와 답이 일치한다면
        print("통과!")
        n += 1
    else :
        print("오타! 다시 도전")

end = time.time() #종료 시간 확인
et = end - start
print(f"타자 시간: {et: .2f}") #et를 소수점 2자리까지 표시