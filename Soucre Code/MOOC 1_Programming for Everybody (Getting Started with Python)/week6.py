# cho người dùng nhập số giờ hrs và số tiền mỗi giờ rps sau đó tính lương, trả gấp 1.5 kể từ giờ thứ 40 trở lên
# dùng hàm computepay()

def computepay(h, r):
    if hrs < 40:
        return h*r
    else:
        return (40*rph+(hrs-40)*(rph*1.5))


hrs = float(input("Enter hours: "))
rph = float(input("Enter rade per hours: "))
pay = computepay(hrs,rph)
print('Pay:',pay)
