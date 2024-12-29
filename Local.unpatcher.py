import sqlite3

def clear_line_content_in_file(filename, line_number):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        if line_number <= len(lines):
            lines[line_number - 1] = "\n"  
            with open(filename, 'w') as file:
                file.writelines(lines)
            
        else:
            print(f"В файле {filename} нет строки под номером {line_number}. Файл был повреждён")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при работе с файлом: {e}")

def delete_table_from_db(database, table_name):
    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        connection.commit()
        connection.close()
        print('Токен удалён из системы, теперь можно получить новый!')
    except sqlite3.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")

if __name__ == "__main__":
    php_file = "m_pref.php"
    db_file = "pref.db"
    line_to_remove = 20
    table_to_remove = "token"
    
    clear_line_content_in_file(php_file, line_to_remove)
    delete_table_from_db(db_file, table_to_remove)
    input('Нажмите Enter чтобы продолжить   .   .   .')
