import sqlite3
# import logging

# logging.INFO()

# A4 бумага
db = sqlite3.connect("Users.db")
# Это наша рука с ручкой
cursor = db.cursor()



def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hoby TEXT
        )
                   """)
    db.commit()
    
create_table()

# CRUD - Созданые - Чтение - Обновление - Удаление

def add_user(name, age, hoby):
    cursor.execute(
        'INSERT INTO users(name, age, hoby) VALUES (?,?,?)',
        (name,age,hoby)
    )
    db.commit()
    print(f"Добавили {name}")
    
add_user("Ardager", 23, "спать")
add_user("Loli", 23, "спать")
add_user("John", 23, "спать")
add_user("Mike", 23, "спать")

def update_user_by_rowid(name=None, age=None, hoby=None, rowid=None):
    if name:
        cursor.execute(
            'UPDATE users SET name = ? WHERE rowid = ?',
            (name, rowid)
        )
    if age:
        cursor.execute(
            'UPDATE users SET age = ? WHERE rowid = ?',
            (age, rowid)
        )
    if hoby:
        cursor.execute(
            'UPDATE users SET hoby = ? WHERE name = ?',
            (hoby, name)
        )
    
    db.commit()
    print('Update success')
        

# update_user_by_rowid(name="Вася", hoby="Гулять")
    

def delte_user_by_rowid(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    db.commit()
    print('DELETE success')
    
# delte_user_by_rowid(2)
    

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(f"-----{users}")
    
    
    if users:
        print("Список всех пользователей")
        for user in users:
            print(f"Name: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")
    else:
        print(f"Список пользователей пуст")

get_all_users()
            


db.close()

