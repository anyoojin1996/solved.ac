# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

words = input().upper()

cnt = dict()
for i in words:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

dup = []
for i in cnt:
    if max(cnt.values()) == cnt[i]:
        dup.append(i)

if len(dup) >1:
    print("?")
else:
    print(dup[0])

