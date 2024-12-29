import random
import string
import sqlite3
import os

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


    file_path = "m_pref.php"

    # Проверка существования файла
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    # Чтение содержимого файла
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Запись новой строки на 19-ю строку
    # Если строк меньше 19, добавляем недостающие строки
    while len(lines) < 19:
        lines.append("\n")  # Добавляем пустые строки, если их не хватает

    # Заменяем 19-ю строку
    lines[18] = f"$spToken = '{token}';\n"

    # Запись обратно в файл
    with open(file_path, "w") as file:
        file.writelines(lines)

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