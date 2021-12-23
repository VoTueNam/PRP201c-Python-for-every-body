#VoTueNam_CE140557_IA1401
import sqlite3

conn = sqlite3.connect("dbFPT.sqlite") #connect or create a database with name: dbFPT.sqlite
cur = conn.cursor()#create cursor

#execute sql command create table
cur.execute("DROP TABLE IF EXISTS InFos")
cur.execute("CREATE TABLE InFos(ProCode INTEGER, Deleted TEXT)")

#Open file text and insert infomation of this file into database sqlite
fopen = open("datafile.txt") #Open TEXT file
for line in fopen:
	if not line.startswith("ProjectCode"): #Not check the first line in this text file
		line = line.rstrip()
		line = line.split()
		code = line[0] #get ProCode of a line
		deleted = line[3] #get Deleted of a line
        #execute INSERT command sqlite
		cur.execute("INSERT INTO InFos(ProCode, Deleted) VALUES(?,?)", (code, deleted))
conn.commit()

#count number of processed records
cur.execute("SELECT Count(ProCode) FROM InFos")
reader = cur.fetchone() # read database
print("Number of records: "+str(reader[0]))
print("")

#The first 3 row of the table when sorted in descending order by ProjectCode:
print("The first 3 row of the table when sorted in descending order by ProjectCode:")
cur.execute("SELECT * FROM InFos ORDER BY ProCode DESC LIMIT 3")
result = cur.fetchall() # read database
for x in result:
	print(str(x[0])+" "+str(x[1]))
#close cursor
cur.close()
