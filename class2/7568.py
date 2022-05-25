num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ") 
    # 나보다 키와 몸무게 둘다 큰애가 몇명이나 있는지 확인하면 등수가 됨