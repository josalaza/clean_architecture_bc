import mysql.connector
from base_datos import BaseDatos

class MySQL(BaseDatos):
    def __init__(self, host, user, password, database, port):

        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        self.cursor = self.conn.cursor()

    def guardar(self, datos):
        if self.conn and self.cursor:
            self.cursor.execute("SELECT * FROM bancolombia.user_traits")
            self.conn.commit()
        else:
            print("No se pudo conectar ")

    def leer(self):
        if self.conn and self.cursor:
            self.cursor.execute("SELECT contenido FROM datos")
            return [row[0] for row in self.cursor.fetchall()]
        else:
            print("No se pudo conectar .")
            return []
