import matplotlib.pyplot as plt

data = []
with open('學生成績.csv') as f:
    text = f.read().split()
    cap = text[0].split(',')  #各項成績名稱
    for i in text[1:]:
        stu = i.split(',')
        scores = [float(sc) for sc in stu[1:]]
        data.append([stu[0]] + scores)
print(stu)

# #繪製曲線圖
# for stu in data:
#     name = stu[0]
#     scores = stu[1:]
#     plt.clf()  #設定全新圖表(若無此行，學生成績會不斷疊加在同張圖表)
#     plt.plot(scores, marker='o')  #若只傳入一個列表，會預設作為y軸的值
#     plt.title(name)
#     plt.xticks(range(len(scores)), cap[1:])  #(刻度,顯示文字)
#     plt.xlabel('Item')
#     plt.ylabel('Scores')
#     plt.ylim(0, 110)
#     plt.tight_layout()  #將整個圖表限縮在圖片中
#     plt.savefig(name + '.png')  #存成png
#     plt.show()


#繪製全班平均的比對圖表
avg = []
for e in range(1, len(data[0])):
    all_scores = [data[stu][i] for stu in range(len(data))]
    avg.append(sum(all_scores)/len(all_scores))

plt.plot(scores, marker='o',  label='Your Score')
plt.plot(avg, marker='x', label='Class Average')
plt.legend()  #當有設定label時，需呼叫legend()函式
