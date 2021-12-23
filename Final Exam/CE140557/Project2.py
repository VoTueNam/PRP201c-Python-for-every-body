#VoTueNam_CE140557_IA1401

class Student: #create new class
	#constructor method
	def __init__(self, name, age, mark):
		self.name = name
		self.age= age
		self.mark= mark

	#getter, setter
	def set_name(self, name):
		self.name = name
	def get_name(self):
		return self.name
	def set_age(self, age):
		self.age = age
	def get_age(self):
		return self.age
	def set_mark(self, mark):
		self.mark = mark
	def get_mark(self):
		return self.mark

#display list of student
def display_student(list_Stu):
	for i in range(len(list_Stu)):
		stu = list_Stu[i]
		print("Name: {}, Age: {}, Test_scores: {}".format(stu.name, stu.age, stu.mark))

#add new object student into list
def add_student(stu, list_Stu):
 	list_Stu.append(stu)

#sort list of student by name and order in the alphabet table
def sort_student(list_Stu):
	List_Sort = list()
	for i in range(len(list_Stu)):
		List_Sort.append((list_Stu[i].name, list_Stu[i].age, list_Stu[i].mark))#add infomation of a student into a new list
	List_Sort.sort(key=lambda x:x[0])	#sort by name
	return List_Sort	#return a list of sort student

#Main method
def main():
    #Check valid input number of student
	while True:
		try:
			n = int(input("Number of student: "))
			break
		except: print("Wrong, try again!!!") #catch wrong format number and make try again

	list_Stu = list()
	for i in range(n):
		print("Student number" ,i+1)
		name = input("Name: ")
        #Check valid input age (is number)
		while True:
			try:
				age = int(input("Age: "))
				break
			except: print("Wrong, try again!!!") #catch wrong format number and make try again
        #Check valid input test_scores (is number)
		while True:
			try:
				mark = float(input("Test Scores: "))
				break
			except: print("Wrong, try again!!!") #catch wrong format number and make try again

        #create a object student
		stu = Student(name, age, mark)
        #add a student into a list
		add_student(stu, list_Stu)
		print("")
	print("Before sort: ")
	display_student(list_Stu)
	print("\n")
	print("After sorted by name: ")
	List_Sort = sort_student(list_Stu)
    #print list of student after sort
	for i in List_Sort:
		print("Name: {}, age: {}, test_scores: {}".format(i[0], i[1], i[2]))

if __name__ == '__main__':
	main()
