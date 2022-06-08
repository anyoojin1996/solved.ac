import time

total = int(input()) # 1260

start_time = time.time()
coin_500 = 0
coin_100 = 0
coin_50 = 0

coin_500, total = divmod(total, 500)
coin_100, total = divmod(total, 100)
coin_50, total = divmod(total, 50)
coin_10, total = divmod(total, 10)

end_time = time.time()
print(coin_500 + coin_100 + coin_50 + coin_10)
print('time:', end_time - start_time)



