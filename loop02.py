#Average, Highest & Lowest marks of N students
print("This program is to find the Average, Highest & Lowest marks of N students")
lst = []
num = int(input("Number of students: "))
for n in range(num):
    numbers = int(input("Enter marks "))
    lst.append(numbers)
print("Highest marks in the class is :", max(lst), "\nLowest marks in the class is :", min(lst))
av = (sum(lst) / num)
print("The average marks of", num, "students is:" , av, "marks")





n = int(input("Students: "))
total = 0

for i in range(n):
    marks = int(input("Marks: "))

    if i == 0:
        high, low = marks, marks

    if marks > high:
        high = marks
    if marks < low:
        low = marks

    total += marks


average = total / n

print("Average: ", average)
print("Highest:", high)
print("Lowest:", low)


        
            
