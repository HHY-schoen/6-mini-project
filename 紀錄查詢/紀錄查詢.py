import csv
from collections import Counter  #提供很多資料容器

with open('中華職棒球員打擊數據.csv') as f:
    data = list(csv.DictReader(f))
    results = []
    for i in data:
        if int(i['全壘打']) >= 10 and int(i['盜壘']) >= 10:
            results.append(i)

counts = Counter([i['姓名'] for i in results])
print('共有', len(counts), '人有此成就')

for r, p in enumerate(counts.most_common(3)):
    name, time = p[0], p[1]
    print('第', r+1, '名:', name, '紀錄達成', time, '次')
    for e in results:
        if e['姓名'] == name:
            print(name, e['年度'], e['全壘打'], e['盜壘'])

print('===============')

#年度全壘打+盜壘20
with open('中華職棒球員打擊數據.csv') as f:
    data = list(csv.DictReader(f))
    results = []
    for i in data:
        if int(i['全壘打']) >= 20 and int(i['盜壘']) >= 20:
            results.append(i)
    for e in results:
        print(e['姓名'], e['全壘打'], e['盜壘'])

print('========= 全壘打20 + 打擊率>0.3 ========')
#列出前三個 全壘打20 + 打擊率>0.3 的選手
with open('中華職棒球員打擊數據.csv') as infile:
    data = list(csv.DictReader(infile))
    hits = []
    for e in data:       
        if int(e['全壘打']) >= 20 and float(e['打擊率']) > 0.3:
            hits.append(e)

x = Counter([e['姓名'] for e in hits])  #31
# print(x)
top3 = x.most_common(3)
print(top3)


# for r, p in enumerate(k.most_common(3)):
#     # name, time = p[0], p[1]
#     # print('第', r+1, '名:', name, '紀錄達成', time, '次')
#     for e in hits:
#         if e['姓名'] == name:
#             print(name, e['全壘打'], e['打擊率'])
