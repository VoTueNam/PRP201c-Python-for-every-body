# đọc từng dòng, tìm và phân tích dòng bắt đầu với "From"
# dùng split cắt ra sau đó lấy từ thứ 2 (địa chỉ mail) và in ra
# in số dòng tìm được ra
file = open(input("Enter file name: "))
data = []
for i in file:
    if i.startswith("From"):
        temp = i.split(" ")
        if len(temp) > 2:
            print(temp[1])
            data.append(temp[1])
print("There were", len(data), "lines in the file with From as the first word")
