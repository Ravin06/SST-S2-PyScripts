#Grade Calculator


#User Input
score = int(input("Enter your score: "))
total = int(input("Total: "))

mark = (score / total) * 100

print("Test Score:" , str(mark) + "%")

#Grading
if mark >= 70:
	print("Distinction")
elif mark >=60:
	print("Credit")
elif mark >=50:
	print("Passed")
else:
	print("Failed")
    
