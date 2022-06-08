import time

N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))

start_time = time.time()
total = 0

numbers.sort()
# print(numbers) #[2, 2, 4, 6, 6]

first = numbers[N-1]
second = numbers[N-2]
# print(first, second)

first_score = (M // (K + 1)) * K + (M % (K + 1))
second_score = (M // (K + 1))
total = first_score * first + second_score * second
print("first_score", first_score)
print("second_score", second_score)

end_time = time.time()
print(total)
print('time', end_time - start_time)