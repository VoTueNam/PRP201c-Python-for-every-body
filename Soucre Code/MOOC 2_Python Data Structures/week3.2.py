#cho user nhập tên văn bản
#tính số dòng có nội dung "X-DSPAM-Confidence:    0.8475" và tính giá trị trung bình
file = open(str(input("Enter file name: ")))
total=0.0
count=0.0
for i in file:          #có thể thay thành:     for i in file.readlines():
    if i.startswith("X-DSPAM-Confidence:"):
        count=count+1
        i = i.replace(' ','')
        index = i.find(':')
        total+=float(i[index+1:])
print('Average spam confidence:', total/count)