# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

# a, b, c, d, e, f, g, h, i = map(int, sys.stdin.readline().split())
# max_list = [int(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i)]

import sys

max_list = []
for i in range(1,10):
    input_value = int(input())
    max_list.append(input_value)

max_value = max(max_list)
print(max_value)
print(max_list.index(max_value)+1)