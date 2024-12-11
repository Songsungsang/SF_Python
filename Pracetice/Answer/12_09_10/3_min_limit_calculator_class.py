class Calculator() :
    def __init__(self):
        self.value = 100

    def sub(self, value) :
        self.value -= value

class MinLimitCalculator(Calculator) :
    
    def sub(self, value) :
        self.value -= value
        self.value = max(self.value, 0)
        #slef.value = max(0, self.value - value)
        #super().sub(value) #부모의 sub를 이용하여 값을 구한 후 값을 비교. sub의 값이 복잡할때 사용하면 좋음
        #self.value = max(0, self.value)

cal = MinLimitCalculator()
cal.sub(20)
cal.sub(90)
print(cal.value)