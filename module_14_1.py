# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

# импорт библиотеки SQLite
import sqlite3

# создание и соединение с БД "not_telegram.db"
connection = sqlite3.connect("not_telegram.db")
# создание курсора БД (виртуальная мышь)
cursor = connection.cursor()

# создание БД через SQL-запросы с полями id, username, email, age, balance
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users
(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

# заполнение БД Userы через f-строку
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
    (f'user{i}', f'example{i}@gmail.com', f'{i * 10}', 1000))

# обновление данных БД Users: каждая 2-я запись начиная с 1-й баланс изменен на 500
cursor.execute("UPDATE Users SET balance = ? WHERE id%2 != ?", (500, 0))

# удаление данных БД Users: каждая 3-я начиная с 1-й
for k in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (f'{k}',))

# выборка всех записей БД Users, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for n in users:
    #вывод на консоль в следующем формате
    # Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
    print(f'Имя: {n[0]} / Почта: {n[1]} / Возраст; {n[2]} / Баланс: {n[3]}')

# команда на сохранение изменений БД
connection.commit()
# команда закрытия соединения с БД
connection.close()
