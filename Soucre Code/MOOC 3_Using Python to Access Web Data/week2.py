#tính tổng các số xuất hiện trong văn bản
import re
f = open("demoW2.txt")
listNum = []
for i in f.readlines():
    temp = re.findall("[0-9]+",i)
    listNum.extend(temp)
total = 0
for i in listNum:
    total+=int(i)
print(total)