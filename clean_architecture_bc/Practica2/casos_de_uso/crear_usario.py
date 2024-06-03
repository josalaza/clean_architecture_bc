import clean_architecture_bc.Practica2.entidades.usuario as user
import clean_architecture_bc.Practica2.repositorios.repositorio_usuario as repo

class CrearUsuario:
    def __init__(self, repositorio_usuario: repo.RepositorioUsuario):
        self.repositorio_usuario = repositorio_usuario

    def ejecutar(self, nombre, correo, contraseña):
        usuario_nuevo = user.Usuario(None, nombre, correo, contraseña)
        self.repositorio_usuario.crear(usuario_nuevo)
        return usuario_nuevo