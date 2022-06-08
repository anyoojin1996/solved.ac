# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

num = input()
for i in range(1, int(num)+1): #1부터 범위 지정 안해주면 0으로 들어가서 한줄 띄어쓰기 됨!
    for j in range(1, i+1):
        print('*', end = '') 
    print()

# inp = int(input())
# for i in range(1,(inp+1)):
#     print("*" * i)