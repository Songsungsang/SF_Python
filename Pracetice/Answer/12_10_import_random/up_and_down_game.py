import random

com = random.randint(1, 100)

min_v = 1
max_v = 100
count = 0
score = 100

while True:
    try:
        if count == 10:
            print("시도횟수 초과!!")
            break
        count += 1
        guess = int(input("[%d회]숫자 입력(%d ~ %d): " % (count, min_v, max_v)))
        if guess < 0 or guess > 100:
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답이에요!!")
            print(f"정답 : {com}\n 점수 : {score - ((count-1) * 10)}점")
            break
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
        else:
            print("랜덤수보다 커요")
            max_v = guess
    except ValueError:
        print("숫자만 입력 가능합니다.")