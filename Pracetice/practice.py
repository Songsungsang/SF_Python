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

"""

if 1<3:
    print("True")
    print("True") # 들여쓰기 한 부분까지 if문 조건 달성시 실행
    
print("False")