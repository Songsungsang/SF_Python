"""
def solution(str1, str2):
    answer = 0
    str1_len = len(str1)
    length = len(str2) - str1_len
    for i in range(length+1) :
        if str1 == str2[i:i+str1_len] :
            answer = 1
    return answer
"""
def solution(str1, str2): # 이게 되네
    answer = 0
    if str1 in str2 :
        answer =1
    return answer

a = solution("abc", "aabcc")
b = solution("tbt", "tbbttb")
print(f"A : {a}, B : {b}")