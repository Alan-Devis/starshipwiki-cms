import random
import string
import time
import sqlite3

# Генерация случайной строки
token = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
print('Генерация токена...')
print('Запись токена...')

try:
    # Подключение к базе данных
    conn = sqlite3.connect("pref.db")
    cursor = conn.cursor()

    # Создание таблицы, если её ещё нет
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS token (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT NOT NULL
    )
    """)

    # Вставка значения токена
    cursor.execute("INSERT INTO token (value) VALUES (?)", (token,))

    # Сохранение изменений
    conn.commit()

    print(f'Готово! Ваш токен {token}. Скопируйте его, и вставьте в окно настройки.')
    input('Нажмите ENTER чтобы продолжить   .   .   .')

except sqlite3.Error as e:
    # Вывод ошибки в консоль
    print(f"Произошла ошибка при работе с базой данных: {e}")
    input('Нажмите ENTER чтобы продолжить   .   .   .')

finally:
    # Закрытие соединения, если оно было открыто
    if 'conn' in locals() and conn:
        conn.close()