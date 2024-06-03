import manejador_datos
import mysql_db
import mongodb

def Main():
    mysql_bd = mysql_db.MySQL(host='localhost', user='root', password='root', database='bdmysql', port = '3307')
    manejador_mysql = manejador_datos.ManejadorDatos()
    manejador_mysql.procesar(mysql_bd)

    mongodb_bd = mongodb.MongoDB(uri='mongodb://localhost:27017/', database='mongodb', collection='datos')
    manejador_mongodb = manejador_datos.ManejadorDatos()
    manejador_mongodb.procesar(mongodb_bd)

if __name__ == '__main__':
    Main()