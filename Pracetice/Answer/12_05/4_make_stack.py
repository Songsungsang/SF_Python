import sys

stack = []
functions = ["push", "pop", "size", "empty", "top"]

def push(number) :
    stack.append(number)

def pop() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack.pop())

def size() :
    print(len(stack))

def empty() :
    if len(stack) == 0 :
        print(1)
    else :
        print(0)

def top() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack[len(stack) - 1])

num_input = int(input())
"""
for i in range(num_input):
    command = sys.stdin.readline().split() # 파이썬ㅇ에서 for 문안에 input을 사용하면 시간이 너무 오래 걸리기 때문에 이걸 사용
    if command[0] in functions : 
        if command[0] == "push" :
            push(int(command[1]))
        elif command[0] == "pop" :
            pop()
        elif command[0] == "size" :
            size()
        elif command[0] == "empty" :
            empty()
        else :
            top()
"""

for i in range(num_input):
    command = sys.stdin.readline().split() # 파이썬ㅇ에서 for 문안에 input을 사용하면 시간이 너무 오래 걸리기 때문에 이걸 사용
    if command[0] in functions : 
        match command[0] :
            case "push" :
                push(int(command[1]))
            case "pop" :
                pop()
            case "size" :
                size()
            case "empty" :
                empty()
            case _:
                top()