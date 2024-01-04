#末三碼對中即可

win = open('中獎號碼_2.txt').read().split()
mine = open('我的發票_2.txt').read().split()

# for i, num in enumerate(mine):
    # for win_num in win:
    #     if num[-5:] == win_num[-5:]:
    #         print('第', i+1, '張發票對中號碼', num[-5:], '!')
    #     elif num[-4:] == win_num[-4:]:
    #         print('第', i+1, '張發票對中號碼', num[-4:], '!')
    #     elif num[-3:] == win_num[-3:]:
    #         print('第', i+1, '張發票對中號碼', num[-3:], '!')

#對中總金額
get = 0
for i, num in enumerate(mine):
    for win_num in win:
        if num[-5:] == win_num[-5:]:
            get += 4000
        elif num[-4:] == win_num[-4:]:
            get += 1000
        elif num[-3:] == win_num[-3:]:
            get += 200
print('對中總金額: ', get)


#以for句型簡化
count= 0
sum = 0
money = [200,1000,4000]

for i, num in enumerate(mine):
    for win_num in win:
        for r in range(5,1,-1):
            if num[-r:] == win_num[-r:]:
                print('第', i+1, '張對中', r, '碼', win_num[-r:])
                count += 1
                sum = sum + money[r-3]
                break

print('總共中了', count, '張!')
print('總中獎金額', sum, '元!')
