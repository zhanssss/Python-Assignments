# VARIANT C
# C1

import os
print('Checking file...')
if os.path.exists('students.csv'):
    print('file found')
else:
    print('error')
    exit()

print('checking folder...')
if os.path.exists('/output'):
    print('folder found')
else:
    os.makedirs('/output')
    print('folder created')


# C2

import csv
with open('students.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    students = list(reader)

print(f"Total students: {len(students)}")

print("\nFirst 5 rows")
print("-"*30)

for row in students[:5]:
    s_id = row['student_id']
    age = row['age']
    gender = row['gender']
    country = row['country']
    gpa = row['GPA']
    print(f"{s_id} | {age} | {gender} | {country} | GPA: {gpa}")

print("-"*30)


# C3
print("-"*30)
print("Sleep vs GPA Analysis")
print("-"*30)

g1 = []
g2 = []

for row in students:
    sleep_hours = float(row['sleep_hours'])
    gpa = float(row['GPA'])
    if sleep_hours < 6:
        g1.append(gpa)
    if sleep_hours >= 6:
        g2.append(gpa)


avg_g1 = sum(g1) / len(g1)
avg_g2 = sum(g2) / len(g2)

print(f"Students sleeping < 6 hours: {len(g1)}")
print(f"Average gpa (<6 hours): {round(avg_g1, 2)}")

print(f"Students sleeping >= 6 hours: {len(g2)}")
print(f"Average gpa (>=6 hours): {round(avg_g2, 2)}")

print(f"Difference in avg GPA: {round(abs(avg_g1 - avg_g2), 2)}")
print("-"*30)

# C4
import json

result = {
    "analysis" : "Sleep vs GPA",
    "total_students" : len(students),
    "low_sleep": {
        "students": len(g1),
        "avg_gpa": round(avg_g1, 2)
    },
    "high_sleep": {
        "students": len(g2),
        "avg_gpa": round(avg_g2, 2),
    },
    "gpa_difference": round(abs(avg_g1 - avg_g2), 2)
}


print("="*30)
print("ANALYSIS RESULT")
print("="*30)

print(f"Analysis: {result['analysis']}")
print(f"Total students: {result['total_students']}")
print('-'*30)
print("Sleep < 6 hours")
print(f"Students: {result['low_sleep']['students']}")
print(f"Average gpa: {result['low_sleep']['avg_gpa']}")
print("Sleep >= 6 hours")
print(f"Students {result['high_sleep']['students']}")
print(f"Average GPA: {result['high_sleep']['avg_gpa']}")
print("-"*30)
print(f"GPA difference: {result['gpa_difference']}")
print("="*30)

with open('output/result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)

print("Resul saved to output/result.json")
