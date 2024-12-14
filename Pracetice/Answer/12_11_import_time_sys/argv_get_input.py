import sys

args = sys.argv[1:]
print(args)
input = 0
for i in args :
    print(i)
    input += int(i)

print(input)