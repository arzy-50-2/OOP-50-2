import sqlite3

# A4 бумага
db = sqlite3.connect("UsersGrades.db")
# Это наша рука с ручкой
cursor = db.cursor()

# TABLE - Моделька, Сушность, Образ
# Стобцы - поля (Fields)
# 17:00 time
# 28.06.2025 | 2025.06.28 date
# 28.06.2025:10:00:00 + UTC + 6h

def create_tables():
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hoby TEXT
        )
                   """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            subject VARCHAR (100) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(userid)
        )
                   """)
    db.commit()
    print("Таблицы созданы или обновлены")
    
create_tables()



def add_user(name, age, hoby):
    cursor.execute(
        'INSERT INTO users(name, age, hoby) VALUES (?,?,?)',
        (name,age,hoby)
    )
    db.commit()
    print(f"Добавили {name}")
    
add_user("Адекс", 14, "БравлСтарс")
add_user("Апекс", 12, "ТикТок")
add_user("Лия", 13, "Шортс")
add_user("Монро", 15, "СтэндОфф")


def add_grade_for_user(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (user_id,subject,grade)
    )
    db.commit()
    print(f"Добавили {subject} пользователю с id {user_id}")
    
    
# add_grade_for_user(1, "Матем", 5)
# add_grade_for_user(1, "Иностранный", 4)
# add_grade_for_user(3, "Физика", 3)
# add_grade_for_user(4, "ИЗО", 2)
# add_grade_for_user(1, "ООП", 1)



def get_users_with_left_join():
    cursor.execute("""
        SELECT users.name, grades.subject, grades.grade
        FROM users LEFT JOIN grades ON users.userid = grades.userid
                   """)
    
    users = cursor.fetchone()
    print(f"DATA in left join {users}")
    # for user in users:
    #     print(f"FIO: {user[0]} AGE: {user[1]}, subject: {user[2]}, GRADE: {user[3]}")
        
# get_users_with_left_join()        

# Агрегационные функции и группировка данных
# AVG, MAX, MIN

def get_avg_grade():
    cursor.execute('SELECT MIN(grade) FROM grades')
    avg_grade = cursor.fetchall()
    print(f"AVG GRADE: {avg_grade}")
    

# get_avg_grade()

# Views (пердставления)

def get_young_users_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS get_alfa AS
        SELECT name, age
        FROM users
        WHERE age <= 15
                   """)
    db.commit()
    print("View create or update")
    
get_young_users_view()


def alfa_users():
    cursor.execute('SELECT * FROM get_alfa')
    users = cursor.fetchall()
    
    for user in users:
        print(f"Name: {user[0]} Age: {user[1]}")
        

alfa_users()
