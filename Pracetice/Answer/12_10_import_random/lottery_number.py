import random

number_set = {random.randint(1,45)} # 빈 set은 dict로 인식되므로 첫 숫자 넣기

while len(number_set) < 6 : # set 크기가 6 미만인 동안
    number_set.add(random.randint(1,45))

number_list = list(number_set) # 중복값 없는 숫자들 리스트에 넣기
number_list.sort()
print(number_list)

lotto = random.sample(range(1,46), 6) # 한줄로 숫자 6개 뽑는 방법
print(sorted(lotto))