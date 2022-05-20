N, M = map(int, input().split())

board = []
repair = []

for i in range(N):
    board.append(input())

for i in range(N-7):
    for j in range (M-7):
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 ==0:
                    if board[k][l] == 'W':
                        first_W += 1
                    else:
                        first_B += 1
                else:
                    if board[k][l] == 'W':
                        first_B += 1
                    else:
                        first_W += 1
        repair.append(first_W) # repair =[first_W, first_B] 말고 append로 해야 계속 이전 것들 누적됨
        repair.append(first_B)

print(min(repair))
            
