import random, time, os, sys

# with open("word.txt", "w") as f:
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#         'grape', 'garlic', 'onion', 'potato']
#     for i in word: # 각 단어마다
#         f.write(i + " ") # 단어들을 한칸 띄우고 하나씩 넣음
#         #f.write(i + "\n")

# with open("word.txt", "r") as f: # 방금 단어들을 채운 파일을 다시 열어서
#     data = f.read().split() #한칸 띄어쓰기 기준으로 쪼개기
#     # data = f.readlines()
#     word = random.choice(data) # 랜덤으로 하나 고르기
#     print(word)

if os.path.exists("./Answer/12_12/word.txt"): #특정 파일이 현재 경로에 있다면
    with open("./Answer/12_12/word.txt", "r") as f:
        word = f.read().split() #한칸 띄어쓰기 기준으로 쪼개기
        # data = f.readlines()
        print(word) # word는 지역변수가 아니라 글로벌이어서 밑에서 사용 가능
else:  #없다면 리스트를 하나 여기서 만듬
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
            'grape', 'garlic', 'onion', 'potato']

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
