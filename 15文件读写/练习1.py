#1.写入文件（使用with自动关闭），写入中文必须使用utf-8
with open('poem.txt','w',encoding='utf-8') as f:
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
print("————读取结果————")
with open('poem.txt','r',encoding='utf-8') as f:
    content = f.read()
    print(content)

s = []
a = 0
with open('scores.txt','r+',encoding='utf-8') as f:
    for l in f:
       """ line = l[:-1]
        if line != '':
            sum.append(int(line))
    for i in sum:
        a = a + i
    print(f"平均数为{a/len(sum)}")"""
       l = l.strip()#去除首位空白字符，包括换行符
       if l:
           s.append(int(l))
    ave = sum(s)/len(s)
    print("平均分为：",ave)