# tìm số lần gửi thư vào các giờ
# lấy ở chuỗi bắt đầu bằng "From" (mail)
# sort theo giờ và in ra
file = open(input("Enter file name: "))
dicTime = dict()
for i in file:
    if i.startswith("From"):
        temp = i.split(" ")
        if len(temp) > 2:
            temp1 = temp[6].split(":")
            if temp1[0] not in dicTime:
                dicTime.update({str(temp1[0]): 1})
            else:
                dicTime.update({str(temp1[0]): dicTime[str(temp1[0])]+1})
temp = dicTime
temp = sorted(temp)
for i in temp:
    print(i, dicTime[i])
