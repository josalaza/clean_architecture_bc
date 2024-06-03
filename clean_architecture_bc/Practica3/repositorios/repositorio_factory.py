import clean_architecture_bc.Practica3.repositorios.repositorio_mysql as mysql

class RepositoryFactory:
    @staticmethod
    def create_user_repository():
        return mysql.MySQLUserRepository(host="localhost", user="root", password="password", database="fluskdb")