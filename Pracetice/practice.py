'''
#print("Hello world")
#print("Hello", "Python")

#print("Hello", 1, 2, "asdfsdf", sep="")
#print("Hello", 1, 2, "asdfsdf", sep=" ")
#print("Hello", 1, 2, "asdfsdf", sep="\n")
#print("안녕하세요", end="___")
#print("코딩온입니다.")
'''

'''
ive = "I AM"
print(ive)
ive = "신뢰에요"
print(ive)
name = "Harin"
name = name + " Victoria"
print(name)
'''

"""
ive = "장원영"
print(f"나는 {ive}입니다.")
print("나는", ive, "입니다.")


print(type(77))
print(type(7.2))
print(type("ive"))

print("iv\'e")
print("iv\"e")

print("111\n111")
print("111'111")
print('111"111')


num = 10
b_num = 0b1010
h_num = 0XA

print(num)
print(b_num)
print(h_num)

print(bin(10))
print(hex(10))


print(3//2)
print(3.25//2)
print(3%2)
print(3.25%2)
print(2**3)
print(2**10)

print(1+(2*(3**2)))
print(1+2*-3**2) # 3의 2제곱이 먼저, 그다음에 - 하고 2 곱해서 -18 + 1이 나옴
print(1+2*(-3)**2) # 이래야 19가 나옴


print("장원영 "+"럭키비키")
print("럭키"*10)



#song = input("너의 최애 노래는?")
#print(song)
#print(type(song))

a = input("1+1?")
#print(a)
print(int(a)*2)

print(str(2)*10)
print(str(2)+"입니다.")


a = []
b = [1,2,3,4]
c = ["장원영", "안유진"]
d = [1, "아이브"] #파이썬의 list는 숫자랑 문자열 둘다 저장 가능
print(len(c))
print(c[0]) #0번째를 출력
c[0] = "카리나"
print(c)
del c[0] #0번째 데이터를 삭제
print(c)
c.append("원영적 사고")
print(c)


seasons = ["봄", "여름", "가을", "겨울"]
print(seasons[0:1])
print(seasons[0:2])
print(seasons[:2])
print(seasons[1:])
print(seasons[2:])
print(seasons[1:3]) #뒤에가 들어가는지 안 들어가는지 헷갈림. 여기는 1,2 출력
print(seasons[::2]) # 시작부터 2간격으로 중간 건너뛰기. 여기는 봄하고 여름 건너뛰고 가을

print(seasons[::-1]) # 뒤집기

seasons2 = ["봄", "여름", "가을", "겨울", [1,2,3,4]]
print(seasons2)
print(seasons2[-1][0]) # 맨 뒤에 1 값을 보기


a = [1,2,3,4,5,6,7,8,9,10]
even = a[1::2]
print(even)
even2 = a[9:0:-2]
print(even2)


a = [3,4,1,2]
a.sort()
print(a)

b = ["a", "c", "b", "d"]
b.sort()
print(b) #정렬된 a b c d 로 나옴= ["1", "10", "2"]
c.sort()
print(c) #1, 10, 2의 결과. 숫자가 아니라 string이기 때문에 사전 순서로 1부터 정렬되고 2가 나오는 모습

print("오늘은 12월 %d일 입니다." % 2)
print("오늘은 %d월 %d일 입니다." % (12,2))
print("오늘은 %d%s %d일 입니다." % (12,'월',2))
print(f"오늘은 {12}{'월 '}{2}일 입니다.") #가장 깔끔한 느낌
print("오늘은 "+str(12)+"월 "+str(2)+"일 입니다.")
print("오늘은 ",12,"월 ",2,"일 입니다.",sep="")

print("Hello".upper())
print("Hello".lower())

friends = "고찬국 김다운 김민창"
a = friends.split("김") #기본 값이 띄어쓰기
print(a)

sentence = "{}월 {}일".format(12,2) #{} 안에 0,1 없어도 가능. 없으면 순서대로
print(sentence) #print(f)를 더 잘 쓰기는 한데 알아서 나쁠건 없다


b = "   111 222   "
print(b.lstrip()) #111 222   
print(b.strip()) #111 222
print(b.split())


print(1==2)

x = 2
print(1<x<3,"\n")
print(True and False)
print(True or False)
print(not True)


cart = ["계란", "마늘", "콩나물", "커피"]
print("두부" in cart)
print("계란" in cart)



if 1<3:
    print("True")
    print("True") # 들여쓰기 한 부분까지 if문 조건 달성시 실행
    
print("False")



i = int(input("어디까지 계산할까요? "))
total_1 = 0
total_2 = 0
for num in range(1, i+1):
    total_1 += num
    if num % 2 != 0 :
        total_2 += num
print(total_1)
print(total_2)



a = [10, 20, 30]
print(sum(a))

a = [1,2,3,4,5]
a3 = [i * 3 for i in a]
print(a3) # 3,6,9,12,15

a4 = [i * 3 for i in a if i % 2 == 0] # i에 if로 조건을 넣는것도 가능
print(a4) # 2*3, 4*3


for y in range(3): # 이중 for 문
    for x in range(2): # 안쪽 x for문에서 돌림
        print(f"y:{y}, x:{x}")
    print("") # y 쪽에서 돌리기


for i in range(2, 10):
    print(f"[{i}] 단")
    for j in range(1,10):
        print(f"{i} * {j} = {i * j}")
    print("")



customer = int(input("고객수 입력: "))
row = int(input("좌석행 수 입력 : "))

if customer % row == 0 :
    column = customer // row
else :
    column = (customer // row) + 1

for i in range(0, row) :
    for j in range(1, column + 1) :
        seat = i * column + j
        if seat > customer :
            break
        print(seat, end = " ")
    print("")



t1 = (10, 20, 30)
print(type(t1))
print(t1)
print(t1[0])
del t1 # 튜플 자체를 지우는건 가능

t2 = (10)
t3 = (10,)
t4 = 10,
print(type(t4))



set1 = {1,2,3}
print(set1)
set2 = set([1,2,3,3])
print(set2)
set2.add(4)
print(set2)
while len(set2) > 0 :
    a = set2.pop() # 값 pop해서 a가 가짐
    print(set2)
    print(a)

l1 = [1,2,3,4]
while len(l1) > 0 :
    a = l1.pop()
    print(a)

set3 = set("apple")
print(set3)
while len(set3) > 0 :
    a = set3.pop()
    print(a)



name = ["1","2","3","2"]

for i in range(len(name)) :
    if name.count(name[i]) > 1 :
        print(name[i])
        #name.remove(name[i]) 이 코드를 돌려서 remove를 하면 len 값이 바뀌어서 루프가 망가져 오류남

name_set = set(name) #set으로 바꾸면 중복이 제거
print(name_set)
name_list = list(name_set) #다시 list로 바꾸기
name_list.sort() #list에서는 set에서 못하는 sort 가능
print(name_list)


name = ["1","2","3","2"]
set1 = set([])
for i in range(len(name)) :
        print(name[i])
        set1.add(name[i])
a = list(set1)
print(a)


name = ["1","2","3","2"]
a= []
for i in range(len(name)) :
    if a.count(name[i]) < 1 :
        a.append(name[i])
print(a)


a = {} #이건 dictionary dict()
print(type(a))
b = {1} #이건 set set()
print(type(b))
c = dict()
c = {1: 'a', 'b': 'b'}
print(c)
c[2] = 'c' #이렇게 dictionary에 넣는게 가능함
c['c'] = 2
print(c)
del c[2] # 바로 지우는 것도 가능
del c['b']
print(c)
#print(c[2]) #이거는 없을때 에러로
#print(c.get(2)) # 이거는 없을때 None으로 출력


for i in c.keys() :
    print(i, c.get(i))

for i in c.values() : # value로는 key를 얻어올 수 없음. key는 unique 하지만 값은 그러지 않을 수 있음
    print(i, c.get(i))

print('c' in c) # c 라는 key 값이 c라는 dictionary 안에 있는가
print(2 in c.values())



dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
#value = dic.get(word)
#f value: #get으로 단어가 있는지 확인해서 True면 print 하도록
if word in dic :
    print(f'{word}: {dic[word]}')
else :
    print("정의된 단어가 없습니다.")


d = [[10, 20], 
     [30, 40], 
     [50, 60]
     ]



print(d)
print(d[0][0])
print(d[1][1])
d.append([70, 80])
print(d)
d[0][0] = 90
print(d)
"""
"""
#d[1].pop(1) # [30, 40] 중에서 40만 사라져 버림
#del(d[1][1]) # 이것도 40만
#d[1].pop()
print(d)
print(len(d)) # 2차원 안에 행이 4개. 30,40 에서 40 빠져도 1개 취급



d = [[3, 1], [3, 2], [3, 3],
     [3, 4], [3, 5], [3, 6],
     [3, 7], [3, 8], [3, 9]
     ]

#for x, y in d : #열이 두개이고 동일해서 사용 가능
#    print(f"{x} * {y} = {x * y}")

for i in d :
    print(f"{i[0]} * {i[1]} = {i[0] * i[1]}") #전제조건은 무조건 2열이 있다가 필요



def f(x) : # def 함수이름(변수) : 로 함수 정의 가능
    result =  x**2 + 2*x + 1
    return result

print(f(3))



def sayHi() :
    print("Hi")
    print("Hi")
    print("Hi") #return 값이 없어도 함수 사용 가능

sayHi()


x = 10


def func2():
    print("func2", x) #x가 전체적으로 10으로 정의되어 있어서 기본값 10인 느낌

def func():
    x = 20
    y = 11
    print("func1", x, y)
    func2()

def func3(x):
    print("func3", x) #여기의 x는 func3가 받아들인 3을 사용

func()
print("main", x)

func3(3)



def times(l) :
    l2 = [i*2 for i in l]
    return set(l2)

v2 = times([1,2,3,4,5])
print(v2)

def  sum_mul(a , b) :
    sum = a + b
    mul = a * b
    return sum, mul

s, m = sum_mul(2, 3)
print(s, m)



def oneUp() :
    #global x
    #x = x + 1 # 이걸 global x 없이 하면 무조건 오류남. 할당과 동작이 동시에 있어서 뭐가 먼저인지 문제 발생
    y = x + 1
    return y

x = 0
print(oneUp())
print(oneUp())
print(oneUp())



def pr_str(txt, count = 1, count2 = 1) : #default 값이 있는 변수를 앞에 두어야 한다. 아니면 어느게 생략되는지 헷갈리므로
    for i in range(count):
        print(txt)
        print(count2)

pr_str("Hello", 3, 2)
pr_str("Hello", 3)
print()
pr_str("Hello")
print()


def calc_avg(*numbers) : # numbers를 튜플로 받음
    print(type(numbers))
    return sum(numbers)/len(numbers)

print(calc_avg(1,2))
print(calc_avg(1,2,3,4,5))

def a() :
    return 1, 2

print(a())


def intro(**kw) :
    print(type(kw))
    for k, v in kw.items() :
        print(f"{k}: {v}")
    for i in kw :
        print(f"{i}")

intro(name="Alice", age=25, city="NY")


list = [2,4,1,4,6]
list.sort()
print(list)
list2 = [2,4,1,4,6]
print("sorted list2", sorted(list2))
print("list2", list2)

print(eval("1+2*2"))

print(int(4.6+0.5)) # int만 하면 4만 나오니까 0.5 더하고 int로 변환하면 반올림 가능
print(int(4.4+0.5))
print(round(4.5)) # 이걸 쓰면 0.5가 반올림 되지 못했다. 짝수로 바뀐다...?
print(round(4.4))
print(round(4.567)) #이건 5로 올라감
print(round(127,-1))
print(round(127,-2))


def hello():
    print("hello")
    hello() #내가 나를 부르고 또 나를 부르고 무한반복 재귀함수

hello()


x = 0
def hello():
    global x
    x += 1
    if x < 3 :
        print("hello")
        hello() #내가 나를 부르고 또 나를 부르고 무한반복 재귀함수
    else :
        print("hello")

hello()


add = lambda x, y : x + y  #익명 함수, 람다 함수
print(type(add))
print(add(1,2))

def add2(x,y) :
    return x + y

add3 = add2
print(add2(1,2))
print(add3(1,2))


def call_3(func): # function을 input으로 받는 함수
    for i in range(3):
        func()

call_3(lambda:print("hi"))
call_3(lambda:print("hello"))

def download(startedCallback, endCallback): # lambda 두개 받아서 각각 돌리기
    startedCallback()
    # download
    endCallback()

download(lambda:print("다운로드 시작"), lambda:print("완료되었습니다")) # function 두개를 보내기


list(map(int, "1","2","3")) #map은 첫번쨰는 function, 두번째는 값들

result = map(lambda x: 3 * x, [1,2,3,4]) # 1회용으로 사용 = lambda
print(list(result))

li = [-5, 1, 2, -11, 76]

#filter(function or None, iterable)
value = list(filter(lambda x: x < 0, li)) # 필터를 사용하여 True 값들 결과들로 나온걸 밖으로 내놓음
print(value) # -5, -11

value = list(filter(lambda x: x > 10, li)) # 필터를 사용하여 - 값들 결과들로 나온걸 밖으로 내놓음
print(value) # 76

value = list(filter(lambda x: x > 3, (map(lambda x: x * 2, li)))) # list를 먼저 2배로 하고 거기서 3 이상을 필터링
print(value)                                                      # map으로 function의 결과를 임시 리스트에 처리


a = dict() # dict, set는 사실 class다
b = set()

class new_class : #붕어빵 틀
    pass

c = new_class() #붕어빵
bb2 = new_class()
bb3 = new_class()

class Movie :
    title = "곡성"

movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)
print()

movie1.title = "태풍을 부르는 영광의 불고기 로드"
print(movie1.title)
print(movie2.title)

movie1.score = "1"
print(movie1.score)
#print(movie2.score)


class Movie :
    name = ''
    def print_msg(msg) :
        print(msg)
    def modify(self, movie) :
        self.name = movie
    def print_name(self) :
        print(self.name)

movie1 = Movie()
movie2 = Movie()

Movie.print_msg("Print하기")
movie1.modify("Print했음")
movie1.print_name()
movie2.modify("극한직업")
movie2.print_name()
print("Movie2 name :", movie2.name)


class Movie:
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience

movie1 = Movie("파묘", 100)
movie2 = Movie("극한직업", 200)
print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)
#movie3 = Movie() # title과 audience가 필요


class Movie:
    count = 0
    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie.count += 1

movie1 = Movie("파묘", 100)
movie2 = Movie("극한직업", 200)

print(movie1.count) # 모든 값들의 count가 2로 바뀜. 다른 값에도 영향을 미친다
print(movie2.count)
print(Movie.count)
print()
Movie.count += 1
print(movie1.count)
print(movie2.count)
print(Movie.count)
print()
movie1.count += 1
print(movie1.count)
print(movie2.count)
print(Movie.count)
print()
Movie.count += 1 #movie1에서 따로 증가를 했어도 무시하고 4,4,4가 나온다. 틀 자체가 바뀌기 때문
print(movie1.count)
print(movie2.count)
print(Movie.count)


class Movie:
    count = 0
    def __init__(self, title, audience) :
        self.__title = title
        self._audience = audience
        Movie.count += 1

    def get_title(self):
        return self.__title
    def set_title(self, title) :
        self.__title = title
    def get_audience(self):
        return self._audience

movie1 = Movie("파묘", 100)
#print(movie1.__title) # 밖에서 접근은 안됨
print(movie1.get_title()) # class안에서 접근하는건 가능
#movie1.__title = "오겜" # 밖에서 set title 없이 접근이... 됨?
#print(movie1.get_title()) # 나오는 이름 파묘로 바뀌지 않은 모습
#print(movie1.__title) # 안의 private를 참조하는 것이 아닌 새로운 변수가 만들어 진것과 같다

print(movie1._audience) # C언어에서는 보호되지만 파이썬에서는 실질적 제한 없음
print(movie1.get_audience())


class Health :
    def __init__(self, name) -> None:
        self.__name = name
        self.__hlp = 100

    def getName(self) :
        return self.__name
    
    def setHp(self, hp) :
        hp = max(hp, 0) # 0보다 작으면 둘중 최대값 hp를 채택
        hp = min(hp, 100) # 100보다 크면 둘중 최소값 hp를 채택
        self.__hp = hp

    def getHp(self) :
        return "hp " + str(self.__hp)
    
    def exercise(self, hours):
        self.setHp(self.__hp + hours)
        print(f"운동을 {hours}시간 하다")
    
    def drink(self, cups) :
        self.setHp(self.__hp - cups)
        print(f"술을 {cups}잔 마시다")

p1 = Health("나몸짱")
p1.setHp(100)
p1.exercise(5)
p1.drink(2)
print(f"{p1.getName()} - {p1.getHp()}")

p2 = Health("나약해")
p2.setHp(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.getName()} - {p2.getHp()}")


class Employee :
    serial_num = 1000

    def __init__(self, name) -> None:
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name
    
    def __str__(self) -> str: # print(e1)같은 형식을 하였을때 출력값을 return 값으로 보여줌
        return "사번 : {}, 이름 : {}".format(self.id, self.name)

e1 = Employee("최사원")
print(e1)

e2 = Employee("안사원")
print(e2)

e3 = Employee("한사원")
print(e3)

employee = [
    Employee("구름"),
    Employee("별"),
    Employee("행성"),
    Employee("달")


]
print(employee[0])
print(employee[1])
print(employee[2])
print(employee[3])


class Country:
    def __init__(self):
        self.name = "나라이름"
        self.population="인구"
        self.capital="수도"

    def show(self): # show를 Korea에게 상속해줌
        print("국가 클래스의 메소드")

class Korea(Country) :
    def __init__(self, name):
        self.name = name

    def show(self) :
        print("국가 이름은", self.name)

country = Korea("대한민국")
country.show()
print(country.name)
country.show()


import calc_module # 다른 파일 import 연습. 같은 폴더내에 있어야 한다.

print(calc_module.add(1,2)) # 다른 파일의 짜여진 함수 사용
print(calc_module.sub(1,2))
print(calc_module.mul(1,2))
print(calc_module.div(1,2))

from calc_module import add # add만 import
print(add(1,2))

import calc_module as cm
print(cm.add(1,2))

import math

print(math.floor(3.141592))
print(math.ceil(3.141592))
print(math.sqrt(9))

from math import floor, ceil
print(floor(3.141592))
print(ceil(3.141592))

import random

print(random.randint(1,5)) # 1부터 5까지의 정수
print(random.uniform(1,5)) # 1부터 5까지의 소수점 있는 숫자
print(random.random()) # 0에서 1사이 숫자
print(random.randrange(1,5)) # 5는 포함이 안됨
print(random.randrange(1,5,2)) #2의 간격으로 출력


import datetime # 시간 관련

now = datetime.datetime.today()
print(now) # 지금의 년월날시분초
print(now.year, now.month) #년, 월 따로 나눠서

print(f"{now.hour}시 {now.minute}분 {now.second}초") # 시분초도 이렇게 나눠서 보여주기 가능

today = datetime.date.today()
print(today.year)

print("지금까지 몇 일?")
first_day = datetime.date(2024, 11, 25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)
print(f"개강 이후 {passed_time.days}일 지났습니다.")


import calendar

#calendar.prcal(2024) # 2024년도 달력 출력
#calendar.prmonth(2024, 12)
#print(calendar.weekday(2024, 12 ,9)) # 2024년 12월 9일이 무슨 요일인가

import datetime

days =['월', '화', '수', '목', '금', '토', '일']
weekday = datetime.date.today().weekday()
print("오늘은 " + days[weekday] + "요일")

def getWeekday(yyyy, mm , dd):
    days =['월', '화', '수', '목', '금', '토', '일']
    weekday = datetime.date(yyyy, mm, dd).weekday()
    print(f"{yyyy}년 {mm}월 {dd}일 {days[weekday]}요일")

getWeekday(2024, 12, 11)


import time

a = time.time()
time.sleep(2)
b = time.time() # 2초 쉬었다가 출력
# print(b-a)

#print(time.localtime())
time_str = time.localtime()
print(time_str.tm_year)

print(time.ctime())
print(time.ctime(a))
print(time.ctime(b))

year = round(time.time()/(365*24*60*60)) # 초가 기준이니 년을 초로 변환해서 나눔
print(year) # 70년도로 부터 약 55년이 흘렀다
days = round(time.time()/(24*60*60)) # 초가 기준이니 일을 초로 변환해서 나눔
print(days) # 70년도로 부터 약 20068일이 흘렀다


import time

def check_time(func): # 함수를 인풋으로 받음
    start = time.time() #시작 시간

    func()

    end = time.time()
    print(f"수행시간 : {end-start}초")

def ten_seconds():
    for i in range(10):
        print(i)
        time.sleep(1)

def hundred_seconds():
    for i in range(100):
        print(i)
        time.sleep(1)

#check_time(ten_seconds)
check_time(hundred_seconds)


import os # 이런게 있구나 넘어가기

os.chdir("C:\\Users\\USER\\git\\SF_Codes\\SF_Python") # 유니코드의 경로지정에는 \ 하나가 아니라 두개 필요
#dir = os.popen('git status')
dir = os.popen('where cat')
print(dir.read())

print(os.listdir())


from modules.mylib import food # 이 파일에서 modules폴더로 들어가서 mylib 폴더로 들어가서 food.py를 조회함
                                #import 하려는 파일의 위치 매우 종요

print(food.name)
food.cook()
food.eat()

from modules.mylib.food import name, cook, eat, mukbang

print(name)
cook()
eat()

import bbb.cm2
print(bbb.cm2.add(1 ,2))

import bbb.cm2 as bc
print(bc.add(1 ,2))


f = open("text.txt", "w")
f.write("Hello World\n")
f.close()


f = open("text.txt" , "w") # 내가 파일을 실행한 위치에 text.txt 생성
print(f.write("Hello World\n"))
f.close()

f2 = open("text.txt") # 기본은 read
#print(f2.read(5))
f2.close()

f3 = open("text.txt", "a") # a 옵션은 뒤에 추가하는거
f3.write("Hello world 22\n")
f3.close()

f4 = open("text.txt")
print(f4.readlines()) # 모든 줄들을 읽어들임
#print(f4.readline(),end="") # 한줄, 1 line씩 읽어들임
#print(f4.readline(),end="")
f4.close()

f4 = open("text.txt", "w")
f4.write("123456789")
f4.close()

f5 = open("text.txt", "r+") # + 파일을 수정하게 위해서 열기
str5 = f5.read()
#f5.seek(4) # seek 0 을 하면 처음으로 다시 올라감
f5.seek(str5.find('5')) # 파일의 텍스트에서 5의 위치를 찾음
print(f5.write("8")) # seek 4로 0에서부터 4번 위치로 간후에 write 8로 한글자만 수정함
f5.seek(0)
print(f5.read())
f5.close()

f4 = open("text.txt", "w")
f4.write("123456789")
f4.close()

with open("text.txt", "r+") as f7:
    str7 = f7.read()
    #f5.seek(4) # seek 0 을 하면 처음으로 다시 올라감
    f7.seek(str7.find('5')) # 파일의 텍스트에서 5의 위치를 찾음
    print(f7.write("8")) # seek 4로 0에서부터 4번 위치로 간후에 write 8로 한글자만 수정함
    f7.seek(0)
    print(f7.read())

import sys, os
if os.path.exists("./output/input.txt") == False: #output 폴더안에 input.txt가 없다면
    with open("./output/input.txt", "w") as f:
        f.write("")
        f.close()

with open("./output/input.txt", "a") as f:
    while True:
        text = input("저장할 내용을 입력해 주세요.(종료-z) : ")
        if text.lower() == "z" :
            break
            # sys.exit(0)
        f.write(text + "\n")


with open("./output/data.bin", "wb") as f:
    txt = "안녕"
    f.write(txt.encode())

with open("./output/data.bin", "rb") as f:
    data = f.read()
    print(data)
    print(data.decode())

with open("./output/question.png", "rb") as f1:
    img = f1.read()

with open("./output/question_copy.png", "wb") as f2:
    f2.write(img)


try:
    num = int(input("정수입력 "))
except ValueError as msg: #값 오류
    print(msg)

try:
    num = int(input("정수입력 "))
except: # 오류라면
    print("뭔진 모르겠지만 에러")

try:
    num = int(input("정수입력 "))
except Exception as msg: #모든 종류의 에러 메세지 출력가능
    print(msg)
else:
    print("예외 없음")

try:
    num = int(input("정수입력 "))
except Exception as msg: #모든 에러의 부모이고 except가 Value가 위에 있으니 ValueError보다 우선
                        #보통 Exception은 가장 포괄적이기 때문에 아래에 두는게 좋다
    print(msg)
except ValueError as msg:
    print("ValueError", msg)
else:
    print("예외 없음")

try:
    num = int(input("정수입력 "))
except Exception as msg:
    print(msg)
except ValueError as msg:
    print("ValueError", msg)
finally: #try가 성공하든 except로 가든 break로 루프를 빠져나가든 무조건 실행
    print("무조건 무조건이야")


a = 1
try :
    a += 1
    if a > 1:
        raise Exception
    a += 2 # 현재 조건에서 Exception으로 무조건 빠지므로 실행안됨
    print("a", a)
except :
    print("error", a) # 강제로 except로 빠짐
"""

class Animal :
    def breath(self) :
        print("숨을 쉰다")
    def cry(self) :
        raise NotImplementedError # 특정 함수를 무조건 override 시켜야 할때

class Dog(Animal) :
    pass

class Cat(Animal) :
    def cry(self) :
        print("야옹")

c = Cat()
c.breath()
c.cry()

d = Dog()
d.breath()
d.cry() # Dog에서 cry를 override 안하면 에러 발생시키겠다