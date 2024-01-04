import csv

results = []
with open('學生成績.csv') as f:
    data = f.read().split()
    for g in data[1:]:
        stu = g.split(',')
        scores = [int(sc) for sc in stu[1:]]
        exam = scores[3]*0.2 + scores[4]*0.3
        hw = sum(sorted(scores[0:3][1:]))/2
        final = round(hw*0.5 + exam, 2)
        # print(stu[0], scores, '作業平均', hw, '總分', final)
        stu.append(final)
        results.append(stu)

#輸出檔案
# with open('新學生成績.csv', 'w') as file:
#     file.write(data[0] + ',總成績\n')
#     for stu in results:
#         file.write(','.join([str(e) for e in stu]) + '\n')


#使用者自行決定計算比重
hw = 90
exam = 80
hw_weight = float(input('請輸入作業比重:'))
final = hw*hw_weight + exam*(1 - hw_weight)
print(hw, exam, final)