
num = int(input())

weight = []
tall = []

rank = 1
rank_list = []

dup = 1

for i in range(num):
    temp = list(map(int, input().split()))
    weight.append(temp[0])
    tall.append(temp[1])
    rank_list.append(0)

while True:
    if max(weight) == 0 and max(tall) == 0:
        break
    else:
        if weight.index(max(weight)) == tall.index(max(tall)):
            if rank == 1:
                temp_index = weight.index(max(weight))
                rank_list[temp_index] = rank
                weight[temp_index] = 0
                tall[temp_index] = 0
                rank += 1
                dup += 1

            else:
                temp_index = weight.index(max(weight))
                rank_list[temp_index] = dup
                weight[temp_index] = 0
                tall[temp_index] = 0
                rank = dup
                rank += 1

        else:
            weight_index = weight.index(max(weight))
            tall_index = tall.index(max(tall))
            a = [i for i in weight if i >= weight[tall_index]]
            b = [i for i in tall if i >= tall[weight_index]]

            for i in a:
                rank_list[weight.index(i)] = rank
                weight[weight.index(i)] = 0
            for i in b:
                rank_list[tall.index(i)] = rank
                tall[tall.index(i)] = 0

            dup += len(a)

print(*rank_list)
            

