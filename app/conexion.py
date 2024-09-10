import mysql.connector
from mysql.connector import Error
from flask import g, current_app
from config import Config

def get_db():
    if 'db' not in g:
        try:
            g.db = mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
                charset="utf8mb4",
                collation='utf8mb4_general_ci'
            )
            g.cursor = g.db.cursor(dictionary=True)
        except Error as e:
            current_app.logger.error(f"Error al conectar a MySQL: {e}")
            return None, None
    return g.cursor, g.db

def close_db(e=None):
    db = g.pop('db', None)
    cursor = g.pop('cursor', None)

    if cursor:
        cursor.close()
    if db:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)