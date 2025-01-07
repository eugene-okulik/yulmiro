import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAM')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as file_csv:
    file_data = csv.DictReader(file_csv)
    data = []
    for row in file_data:
        data.append(row)

query = """
    SELECT s.id 
    FROM `groups` g 
    JOIN students s ON g.id = s.group_id
    LEFT JOIN books b ON s.id = b.taken_by_student_id
    LEFT JOIN marks m ON m.student_id = s.id
    LEFT JOIN lessons l ON l.id = m.lesson_id
    LEFT JOIN subjets s2 ON l.subject_id = s2.id
    WHERE s.name = %s
      AND s.second_name = %s
      AND g.title = %s
      AND b.title = %s
      AND s2.title = %s
      AND l.title = %s
      AND m.value = %s
"""
for row in data:
    params = (
        row['name'],
        row['second_name'],
        row['group_title'],
        row['book_title'],
        row['subject_title'],
        row['lesson_title'],
        row['mark_value']
    )
    cursor.execute(query, params)
    stud_id = cursor.fetchone()
    if stud_id is None:
        print(row)
