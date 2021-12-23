#cho người dùng nhập điểm từ 0.0 đến 1.0 sau đó xếp loại, nếu ngoài khoảng này thì báo lỗi
score = float(input("Enter score: "))
if score<0.0 or score >1.0:
    print('error')
elif score >=0.9:
    print("A")
elif score >=0.8:
    print("B")
elif score >=0.7:
    print("C")
elif score >=0.6:
    print("D")
elif score <0.6:
    print("F")

    
