import sqlite3

class AdaptadorBaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect('clean_arq.db')
        self.conexion.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT NOT NULL,
             correo TEXT NOT NULL,
             contraseña TEXT NOT NULL);''')
        self.conexion.commit()

    def ejecutar_query(self, query, parametros):
        cursor = self.conexion.cursor()
        cursor.execute(query, parametros)
        self.conexion.commit()
        return cursor.lastrowid