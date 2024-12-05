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

"""

def oneUp() :
    #global x
    #x = x + 1 # 이걸 global x 없이 하면 무조건 오류남. 할당과 동작이 동시에 있어서 뭐가 먼저인지 문제 발생
    y = x + 1
    return y

x = 0
print(oneUp())
print(oneUp())
print(oneUp())