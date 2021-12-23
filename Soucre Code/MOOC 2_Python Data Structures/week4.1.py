# mở file ra và đọc TỪNG DÒNG
# tại mỗi dòng cắt các từ ra và cho vào list dùng splist()
# nếu có từ trùng thì không thêm vô nữa
# sort và in list ra
file = open(input("Enter file name: "))
listW = []
for i in file.readlines():
    tempList = i.strip().split(" ")
    for j in range(len(tempList)):
        if tempList[j] not in listW:
            listW.append(tempList[j])
print(sorted(listW))
