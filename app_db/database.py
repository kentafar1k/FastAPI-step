import sqlite3
import os

def init_db():
    """Инициализация базы данных и создание таблицы users"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Создаем таблицу users, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Инициализируем базу данных при импорте модуля
init_db()