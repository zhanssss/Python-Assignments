# Variant C

# a

name = input("Enter student name: ")
math = float(input("Enter Math grade: "))
phy = float(input("Enter Physics grade: "))
py = float(input("Enter Python grade: "))

# b

average = (math + phy + py) / 3
scholarship = 0
if average >= 90:
    scholarship = 35000
else:
    scholarship = 0
gpa = average / 25

# c

print("==============================")
print("     STUDENT REPORT CARD      ")
print("==============================")
print("Student: ", name)
print("Math Grade: ", math)
print("Physics Grade: ", phy)
print("Python Grade: ", py)
print("==============================")
print("Average: ", round(average, 2))
print("Scholarship: ", scholarship)

# d

print("==============================")
print("Scholarship granted", average >= 90)
print("Perfect score", )
print("=============================")

