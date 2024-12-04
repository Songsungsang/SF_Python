students = {'Alice' : 85, 'Bob' : 90, 'Charlie' : 95}
students['David'] = 80
students['Alice'] = 88
students.pop('Bob')
for i in students:
    print(f"{i} : {students[i]}")