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

while M != 0:
    temp_K = K
    while temp_K != 0:
        if M != 0:
            total += first
            temp_K -= 1
            M -= 1
        else:
            break
    if M != 0:
        total += second
        M -= 1

end_time = time.time()
print(total)
print('time', end_time - start_time)
    

