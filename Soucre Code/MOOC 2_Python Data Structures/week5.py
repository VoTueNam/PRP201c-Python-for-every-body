# đọc và tìm ra người gửi nhiều thư nhất
# người gửi là từ thứ 2 ở chuỗi bắt đầu bằng "From" (mail)
# sử dụng Python Dictionary
# sau khi tạo dic rồi thì dùng vòng lặp để tìm ra thằng gửi nhiều nhất
# đọc file demoW4.2.txt
file = open(input("Enter file name: "))
dicName = dict()
for i in file:
    if i.startswith("From"):
        temp = i.split()
        if len(temp) > 2:
            if temp[1] not in dicName:
                dicName.update({temp[1]: 1})
            else:
                dicName.update({temp[1]: dicName[temp[1]]+1})
max = 0
authorMax = ""
for i in dicName:  # khi duyệt nó sẽ duyệt keys
    if dicName[i] > max:
        max = dicName[i]
        authorMax = i

print(authorMax, max)
