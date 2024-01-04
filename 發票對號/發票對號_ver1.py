#另存兩個txt檔(中獎號碼、我的發票)

win = open('中獎號碼_1.txt').read().split()
mine = open('我的發票_1.txt').read().split()

for i, num in enumerate(mine):
    if num in win:
        print('第', i+1, '張發票對中號碼', num, '!')

#中獎張數
count = 0
for i, n in enumerate(mine):
    if n in win:
        count += 1
print(count)

#中獎總金額
sum = 0
for i, n in enumerate(mine):
    if n in win:
        sum += 200
print(sum)