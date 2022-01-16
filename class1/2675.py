# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

# T = int(input())
# for i in range(T):
#     R_1, S_1 = input().split()
#     R_2, S_2 = input().split()

# for i in list(S_1):
#     if list(S_1).index(i) == len(list(S_1))-1:
#         print(i*int(R_1))
#     else:
#         print(i*int(R_1), end='')


# for i in list(S_2):
#     if list(S_2).index(i) == len(list(S_2))-1:
#         print(i*int(R_2))
#     else:
#         print(i*int(R_2), end='')


# T = int(input())
# T_1 = []
# T_2 = []
# for i in range(T):
#     R, S = input().split()
#     T_1.append(int(R))
#     T_2.append(S)

# print('T_1', T_1)
# print('T_2', T_2)


# for j in range(T):    
#     for i in T_2[j]:
#         if list(T_2[j]).index(i) == len(list(T_2[j]))-1:
#             print(i*T_1[j])
#         else:
#             print(i*T_1[j], end='')

#정답 (입력 한번-출력 한번 이런식으로 해야됨)
n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김



