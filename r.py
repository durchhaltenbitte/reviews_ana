data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))

print('文件读取结束，共',len(data), '笔留言。')
#算留言的平均长度
sum_len = 0
for d in data:
    sum_len += len(d)
print('留言平均长度为:', sum_len/len(data))