import sys

class Calculator:
    def __init__(self, a, b) -> None:
        self.__a = a
        self.__b = b
    
    def add(self) :
        return self.__a + self.__b
    
    def sub(self) :
        return self.__a - self.__b
    
    def mul(self) :
        return self.__a * self.__b
    
    def div(self) :
        if self.__b == 0 : #에러 처리
            print("숫자를 0으로 나눌 수 없습니다")
            return sys.exit(0) #에러 처리 나가기
        else :
            return self.__a / self.__b

cal1 = Calculator(5, 3)
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())

cal2 = Calculator(4, 0)
print(cal2.add())
print(cal2.sub())
print(cal2.mul())
print(cal2.div())