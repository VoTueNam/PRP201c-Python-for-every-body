# cho người dùng nhập số cho đến khi người dùng nhập "done" thì dừng lại
# nếu người dùng nhập gì không hợp lệ thì hiện thông báo "Invalid input"
# in ra min và max
min = None
max = None
while True:
    value = input("Enter a number: ")
    if value == "done":
        break
    try:
        value = int(value)
        if min == None or value < min:
            min = value
        elif max == None or value > max:
            max = value
    except:
        print("Invalid input")
print("Min:", min)
print("Max:", max)
