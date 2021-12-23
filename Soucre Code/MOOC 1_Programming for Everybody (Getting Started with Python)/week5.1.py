#cho người dùng nhập số giờ hrs và số tiền mỗi giờ rps sau đó tính lương, trả gấp 1.5 kể từ giờ thứ 40 trở lên
hrs = float(input("Enter hours: "))
rph = float(input("Enter rade per hours: "))
if hrs<40:
    print('Pay:',hrs*rph)
else:
    print('Pay:',40*rph+(hrs-40)*(rph*1.5))

