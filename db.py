import sqlite3

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


def insert(user_id: int, user_name: str, user_surname: str, username: str):
    """
    Добавить пользователя в таблицу
    :param user_id: id пользователя
    :param user_name: Имя
    :param user_surname: Фамилия
    :param username: Никнейм
    """
    cursor.execute('INSERT INTO database (user_id, user_name, user_surname, username) '
                   'VALUES (?, ?, ?, ?)'
                   , (user_id, user_name, user_surname, username))
    conn.commit()


def get(user_id: int):
    """
    Получить пользователя по его id
    :param user_id: id пользователя
    :return: строчка пользователя из таблицы
    """
    cursor.execute('SELECT * FROM database WHERE user_id = ?'
                   , (user_id, ))
    return cursor.fetchall()


def get_all():
    """
    Получить всех пользователей из таблицы
    :return: Массив всех строк пользователей
    """
    cursor.execute('SELECT * FROM database')
    return cursor.fetchall()


def delete(user_id: int):
    """
    Удалить пользователя из таблицы
    :param user_id: id пользователя
    """
    cursor.execute('DELETE FROM database WHERE user_id = ?'
                   , (user_id, ))
    conn.commit()
