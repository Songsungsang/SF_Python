def solution(myString):
    answer = []
    stringList = myString.split("x")
    for i in stringList :
        answer.append(len(i))
    return answer