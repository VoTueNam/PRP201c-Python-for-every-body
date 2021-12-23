#cho user nhập tên văn bản
#load nội dung văn bản lên và in hoa 
fileName = input("Enter file name: ")
try:
    f = open(fileName,"r")
    print(f.read().upper())
except:
    print("File name invalid!")
