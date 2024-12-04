"""
문제
총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.


N_and_M = input()
N_M = N_and_M.split()
N = int(N_M[0])
M = int(N_M[1])
N_list = [] #리스트로 백준 문제를 풀게하니 소요시간이 어마어마하게 커졌었다
M_list = []

for i in range(N) :
    word_input = input()
    N_list.append(word_input)
for i in range(M) :
    word_input = input()
    M_list.append(word_input)

num = 0
for i in range(M) :
    if M_list[i] in N_list :
        num += 1
print(num)


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())
ans = 0
for _ in range(M):
    t = input()
    if t in S:
        ans+=1
print(ans)
"""

N_and_M = input()
N_M = N_and_M.split()
N = int(N_M[0])
M = int(N_M[1])
N_set = set() # set은 사실 내부적으로 Hash를 쓰고 있어서 찾는 속도가 빠름
M_list = []

for i in range(N) :
    word_input = input()
    N_set.add(word_input)
for i in range(M) :
    word_input = input()
    M_list.append(word_input)

num = 0
for i in range(M) :
    if M_list[i] in N_set :
        num += 1
print(num)