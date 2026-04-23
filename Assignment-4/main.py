import os
import csv
import json

def check_files():
    print('Checking file...')
    if os.path.exists('students.csv'):
        print('Checking folder...')
        if not os.path.exists('output'):
            os.makedirs('output')
        return True
    return False


def load_data(filename):
    print('Loading data...')
    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            students = list(reader)
        print(f'Data loaded successfully: {len(students)} students')
    except FileNotFoundError:
        print(f'file {filename} not found')
    return students



def preview_data(students, n=5):
    for row in students[:n]:
        s_id = row['student_id']
        age = row['age']
        gender = row['gender']
        country = row['country']
        gpa = row['GPA']
        print(f"{s_id} | {age} | {gender} | {country} | GPA: {gpa}")


def analyse_sleep_vs_gpa(students):
    low_sleep_gpas = []
    high_sleep_gpas = []

    for row in students:
        try:
            s_id = row['student_id']
            sleep_hours = float(row['sleep_hours'])
            gpa = float(row['GPA'])
        except ValueError:
            print(f'Warning: could not convert value for student {s_id} — skipping row.')
            continue

        if sleep_hours < 6:
            low_sleep_gpas.append(gpa)
        else:
            high_sleep_gpas.append(gpa)

    avg_low_sleep_gpas = sum(low_sleep_gpas) / len(low_sleep_gpas)
    avg_high_sleep_gpas = sum(high_sleep_gpas) / len(high_sleep_gpas)



    return {
        "analysis": "Sleep vs GPA",
        "total_students": len(students),
        "low_sleep": {
            "students": len(low_sleep_gpas),
            "avg_gpa": round(avg_low_sleep_gpas, 2)
        },
        "high_sleep": {
            "students": len(high_sleep_gpas),
            "avg_gpa": round(avg_high_sleep_gpas, 2)
        },
        "gpa_difference": round(abs(avg_low_sleep_gpas - avg_high_sleep_gpas), 2)
    }


if check_files():
    students_list = load_data('student.csv')

    print("\nFirst 5 rows")
    print("-" * 30)
    preview_data(students_list, 5)

    print("-" * 30)
    print("Sleep vs GPA Analysis")
    print("-" * 30)

    result = analyse_sleep_vs_gpa(students_list)

    print(f'Students sleeping < 6 hours: {result["low_sleep"]["students"]}')
    print(f'Average GPA (< 6 hours): {result["low_sleep"]["avg_gpa"]}')

    print(f'Students sleeping >= 6 hours: {result["high_sleep"]["students"]}')
    print(f'Average GPA (>= 6 hours): {result["high_sleep"]["avg_gpa"]}')

    print(f'Difference in avg GPA: {result["gpa_difference"]}')

    print('-' * 30)
    print('Lambda / Map / Filter')
    print('-' * 30)

    low_sleep = list(filter(lambda s: float(s['sleep_hours']) < 6, students_list))
    gpa_values = list(map(lambda s: float(s['GPA']), students_list))
    stressed = list(filter(lambda s: float(s['mental_stress_level']) > 7, students_list))

    print(f'sleep_hours < 6 : {len(low_sleep)} students')
    print(f'GPA values (first 5): {gpa_values[:5]}')
    print(f'mental_stress_level > 7 : {len(stressed)} students')

    print('-' * 30)

    with open('output/result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4)

    print("Result saved to output/result.json")
else:
    print("students.csv file not found")