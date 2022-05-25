# 보통 브루트 포스의 문제의 범위는 1,000,000으로 주어지는 경우가 많다. 
# 코딩테스트 볼 때 범위가 1,000,000이라면 브루트포스를 의심해보자!

#생성자 만드는 법
# num = int(input())

# num_list = list(str(num))
# print(num_list) #['1', '2', '3']

# for i in num_list:
#     num += int(i)

# print(num)

#분해합 만드는 법
num = int(input())

result = 0
check = 0
for i in range(num+1):
    num_sum = list(str(i))
    total = 0
    for j in num_sum:
        total += int(j)

    result = i + total

    if result == num:
        check += 1
        print(i)

if check == 0:
    print(0)
