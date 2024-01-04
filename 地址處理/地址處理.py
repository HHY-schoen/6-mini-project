import csv

with open('地址資料.csv') as f:
    data = list(csv.DictReader(f))
    for i in data:
        print('原始資料: ', i['姓名'], i['縣市'], i['住址'])
        if i['縣市'][0] == '台':
            i['縣市'] = '臺' +i['縣市'][1:]
        if 'F' in i['住址']:
            i['住址'] = i['住址'].replace('F', '樓')
        if i['縣市'] =='臺中市' and '中港路' in i['住址']:
            i['住址'] = i['住址'].replace('中港路', '台灣大道')
        
        print('  更新資料: ', i['姓名'], i['縣市'], i['住址'])
    
        
#  #將修正的資料另存一個新的csv
# with open('新地址資料.csv', 'w', newline='') as file:  #new;ine='' 解決換行問題
#     writer = csv.DictWriter(file, fieldnames=data[0].keys())  #(寫入檔案, 寫入的鍵)
#     writer.writeheader()
#     for i in data:
#         writer.writerow(i)

print('\n=======================')

#統一生日欄位(ex. 83/3/5 -> 83.3.5、西元年改民國年)
a = '83/3/5'
b = a.split('/')
# print(b)
y = int(b[0])
if y > 110:
    y -= 1911
print(str(y) + '.' + b[1] + '.' + b[2])
