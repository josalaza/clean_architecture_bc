import clean_architecture_bc.Practica2.adaptadores.base_datos as bd
import clean_architecture_bc.Practica2.entidades.usuario as user

class RepositorioUsuario:
    def __init__(self):
        self.adaptador = bd.AdaptadorBaseDatos()

    def crear(self, usuario: user.Usuario):
        query = "INSERT INTO usuarios (nombre, correo, contraseña) VALUES (?, ?, ?)"
        parametros = (usuario.nombre, usuario.correo, usuario.contraseña)
        usuario.id = self.adaptador.ejecutar_query(query, parametros)
        return usuario