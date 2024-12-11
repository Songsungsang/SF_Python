import sys

args = sys.argv[1:]
print(args)
args_len = len(args)

#if args_len > 3 or args_len < 3 
if args_len != 3 :
    print("argv의 입력이 3개가 아닙니다")
    sys.exit(0) # 바로 파이썬 프로그램 종료
if args[0] == 'add' :
    result = int(args[1]) + int(args[2])
    print(result)
elif args[0] == 'mul' :
    result = int(args[1]) * int(args[2])
    print(result)
else :
    print("첫 입력이 'mul' 혹은 'add'가 아닙니다")