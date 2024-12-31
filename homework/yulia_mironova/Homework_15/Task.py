import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT into students (name, second_name, group_id) VALUES ('Santa', 'Claus', NULL)")
student_id = cursor.lastrowid
db.commit()

query_book = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('fairy_tale_1', student_id),
    ('fairy_tale_2', student_id),
    ('fairy_tale_3', student_id)
]
cursor.executemany(query_book, values)
db.commit()

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('for_wizards', '30-12-2024', '01-01-2025')")
group_id = cursor.lastrowid
cursor.execute(f'UPDATE students SET group_id = {group_id}  where id = {student_id}')
db.commit()

query_subject = 'INSERT INTO subjets (title) VALUES (%s)'
cursor.execute(query_subject, ('reindeer riding',))
subject1_id = cursor.lastrowid
cursor.execute(query_subject, ('choice of gifts',))
subject2_id = cursor.lastrowid
db.commit()

query_lesson = 'INSERT INTO lessons (title,subject_id) VALUES (%s, %s)'
cursor.execute(query_lesson, ('traffic_rules', subject1_id))
lesson1_id = cursor.lastrowid
cursor.execute(query_lesson, ('deer_care', subject1_id))
lesson2_id = cursor.lastrowid
cursor.execute(query_lesson, ('reading_letter', subject2_id))
lesson3_id = cursor.lastrowid
cursor.execute(query_lesson, ('purchase', subject2_id))
lesson4_id = cursor.lastrowid
db.commit()

query_marks = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
values_2 = [
    (5, lesson1_id, student_id),
    (4, lesson2_id, student_id),
    (3, lesson3_id, student_id),
    (5, lesson4_id, student_id)
]
cursor.executemany(query_marks, values_2)
db.commit()

cursor.execute(f'SELECT * from marks where student_id = {student_id}')
print(cursor.fetchall())

cursor.execute(f'SELECT * from books WHERE taken_by_student_id = {student_id}')
print(cursor.fetchall())

query_all = (f'SELECT * FROM `groups` g join students s on g.id = s.group_id '
             f'left join books b on s.id = b.taken_by_student_id '
             f'left JOIN marks m on m.student_id  = s.id '
             f'left join lessons l on l.id = m.lesson_id '
             f'left join subjets s2 on l.subject_id = s2.id WHERE s.id = {student_id}')

cursor.execute(query_all)
print(cursor.fetchall())

db.close()
