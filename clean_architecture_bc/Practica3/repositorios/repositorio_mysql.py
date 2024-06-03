import mysql.connector
import clean_architecture_bc.Practica3.entidades.entidad_usuario as entity

class MySQLUserRepository:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def find_by_id(self, user_id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            return entity.UserEntity(result['id'], result['name'], result['email'])
        else:
            return None