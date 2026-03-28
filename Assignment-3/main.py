school_info = ("Astana IT University", "Astana", "2025-2026")
# C1
print("="*30)
print(school_info[0])
print(school_info[1] ,"|", school_info[2])
print("="*30)



# C2

names = []
avg = []

for i in range(100):
    student_name = input("Enter student name  (or 'done' to finish):")
    if student_name == "done":
        break
    names.append(student_name)
    m_grade = float(input("Enter Math grade: "))
    ph_grade = float(input("Enter Physics grade: "))
    py_grade = float(input("Enter Python grade: "))
    avg.append((m_grade + ph_grade + py_grade)/3)

print("-"*30)
print("Student records (3 students):")
print("-" * 30)
for i in range(len(names)):
    for j in range(0, len(names) - i - 1):
        if avg[j] < avg[j + 1]:
            avg[j], avg[j + 1] = avg[j + 1], avg[j]
            names[j], names[j + 1] = names[j + 1], names[j]

for i in range(len(names)):
    print(names[i], "avg", round(avg[i], 2))
print("-"*30)

# C3

subjects = set ()
for i in range(100):
    subject_name = input("Enter subject name (or 'done' to finish):")
    if subject_name == "done":
        break
    subjects.add(subject_name)

print("Unique subjects:", len(subjects))
print(subjects)

# C4

print("="*30)
print("CLASS SUMMARY")
print("Astana IT university")
print("="*30)
print("Total students: ", len(names))
print("Class average", round(sum(avg)/len(avg), 2))
print("-"*30)
for i in range(len(names)):
    print(names[i], "avg", round(avg[i], 2))
print("-"*30)

print("Top student: ", names[0], f"({avg[0]})")
print("Lowest student: ", names[-1], f"({avg[-1]})")
print("="*30)


