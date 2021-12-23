#đọc dữ liệu từ mbox.txt và in ra tên tổ chức: số lần gửi mail, sau đó lưu vào database
import re
import sqlite3



conn = sqlite3.connect('demoW2.2.sqlite')	#tạo database nếu chưa có, có rồi thì connect
cur = conn.cursor()							#tạo biến thực thi

cur.execute('''
DROP TABLE IF EXISTS Counts''')				#thực thi câu lệnh SQL (xóa bảng nếu tồn tại)

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = ''
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:								#đọc từng dòng trong file
	if not line.startswith('From: ') : continue	#nếu chuỗi không bắt đầu với From thì quay lại (kiểm tra line tiếp theo)
	pieces = line.split()[1]				#tách line ra và lấy chuỗi ở vị trí thứ 2 (mail)
	org = pieces.split('@')[1]				#tách mail lấy chuỗi ở vị trí thứ 2 (tên tổ chức/sau @)


	print (org)
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))		#lấy số lần gửi theo tên doanh nghiệp
	row = cur.fetchone()												#lấy dòng đầu tiên trong kết quả của câu lệnh Select
	if row is None:														#nếu rỗng thì add tên vào và cho count = 1
		cur.execute('''INSERT INTO Counts (org, count)
				VALUES ( ?, 1 )''', ( org, ) )
	else :										
		cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',	#nếu tồn tại thì cộng 1 vào count
			(org, ))

conn.commit()															#update từ code lên database khi csdl thay đổi


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'	#lấy 10 cái org đầu tiên theo thứ tự count giảm dần

print ("Counts:")
for row in cur.execute(sqlstr) :										#đọc từng dòng trong cơ sở dữ liệu bằng câu lệnh lưu trong sqlstr và lưu vào row
    print (str(row[0]), row[1])

cur.close()
