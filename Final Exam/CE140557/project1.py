#VoTueNam_CE140557_IA1401
import re

#input from user
pwd = input("Input passwords: ")
ls_pass = pwd.split(",")	#bring passwords into a list of password
ls_result = list() #create new list

for password in ls_pass:
	password = password.strip() # delete white space of head and tail of string (password)
	#check length of password is valid: max_length = 12, min_length = 6
	if len(password)>=6 and len(password)<=12:
		#find in this password has at least 1 letter between [a-z]
		lower_letter = re.findall("[a-z]+", password)
		#find in this password has at least 1 number betwwen [0-9]
		number = re.findall("[0-9]+", password)
		#find in this password has at least 1 letter betwwen [A-Z]
		upper_letter = re.findall("[A-Z]+", password)
		#find in this password has at least 1 character from [$#@]
		special_letter = re.findall("[$#@]+", password)
		#check this password is valid
		if len(lower_letter)>0 and len(number)>0 and len(upper_letter)>0 and len(special_letter)>0:
			check=True
		else:
			check=False
	else:
		check=False

	if check==True:
		ls_result.append(password) #add all vaid password above into a new list of passwords


result = "" #create string for print result
print("Valid passwords:")
for i in ls_result:
	result = result + str(i) + ", "
print(result[:-2])
