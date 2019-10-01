
#读取留言 报告结果
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 50000 == 0:
            print(len(data))
print('文件读取结束，共',len(data), '笔留言。')

#算留言的平均长度
sum_len = 0
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
    sum_len += len(d)
print('留言平均长度为:', sum_len/len(data))

#小筛选
print('其中长度小于100的留言有', len(new), '笔。')
good = [d for d in data if 'good' in d]
print('提到good的留言有', len(good), '笔。')
print('例如:', good[0])

#单词计数
wd = {}
for d in data:
    words = d.split()
    # 每条评论中的每个单词分割开来 
    # 清单嵌套 用于计数
    for word in words:
        if word in wd:
            wd[word] += 1
        else:
            wd[word] = 1

# 印字典
# for word in wd:
#     if wd[word] > 10:
#         print(word, ':', wd[word])

#用户查询功能
while True:
    keyword = input('Which word would you like to search?:')
    if keyword == 'q':
        break
    if keyword in wd:
        print(keyword, 'shows', wd[keyword], 'times in all of the', len(data), 'reviews.')
    else:
        print(keyword, 'does not show in all of the', len(data), 'reviews.')

print('感谢您的使用！')



