import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print('Checking file...')
        if os.path.exists(self.filename):
            print(f'File found: {self.filename}')
            return True
        else:
            return False

    def create_output_folder(self, folder='output'):
        print('Checking output folder...')
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f'Output folder created: {folder}')
        else:
            print(f'Output folder already exists: {folder}')


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load_data(self):
        print('Loading data...')
        try:
            with open(self.filename, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.students = list(reader)
            print(f'Data loaded successfully: {len(self.students)} students')
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        return self.students

    def preview_data(self, n=5):
        for row in self.students[:n]:
            s_id = row['student_id']
            age = row['age']
            gender = row['gender']
            country = row['country']
            gpa = row['GPA']
            print(f"{s_id} | {age} | {gender} | {country} | GPA: {gpa}")


class DataAnalyzer:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse_sleep_vs_gpa(self):
        low_sleep_gpas = []
        high_sleep_gpas = []

        for row in self.students:
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

        self.result = {
            "analysis": "Sleep vs GPA",
            "total_students": len(self.students),
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

        return self.result


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)

            print("Result saved to output/result.json")
        except FileNotFoundError:
            print(f"Error: {self.result} not found.")


fm = FileManager('students.csv')

if fm.check_file():
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    students_list = dl.load_data()

    print("\nFirst 5 rows")
    print("-" * 30)
    dl.preview_data(5)

    print("-" * 30)
    print("Sleep vs GPA Analysis")
    print("-" * 30)

    analyzer = DataAnalyzer(students_list)
    result = analyzer.analyse_sleep_vs_gpa()

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

    rs = ResultSaver(result, 'output/result.json')
    rs.save_json()

else:
    print("students.csv file not found")