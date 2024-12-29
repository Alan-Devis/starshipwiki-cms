import random
import string
import sqlite3
import os

token = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
print('Генерация токена...')
print('Запись токена...')

try:
    conn = sqlite3.connect("pref.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS token (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT NOT NULL
    )
    """)

    cursor.execute("INSERT INTO token (value) VALUES (?)", (token,))

    conn.commit()


    file_path = "m_pref.php"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    with open(file_path, "r") as file:
        lines = file.readlines()

    while len(lines) < 20:
        lines.append("\n")  

    lines[19] = f"$spToken = '{token}';\n"

    with open(file_path, "w") as file:
        file.writelines(lines)

    print(f'Готово! Ваш токен {token}. Скопируйте его, и вставьте в окно настройки.')

    input('Нажмите ENTER чтобы продолжить   .   .   .')

except sqlite3.Error as e:
    print(f"Произошла ошибка при работе с базой данных: {e}")
    input('Нажмите ENTER чтобы продолжить   .   .   .')

finally:

    if 'conn' in locals() and conn:
        conn.close()