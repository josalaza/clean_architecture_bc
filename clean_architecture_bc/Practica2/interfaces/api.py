from flask import Flask, request, jsonify
import clean_architecture_bc.Practica2.casos_de_uso.crear_usario as use_case
import clean_architecture_bc.Practica2.repositorios.repositorio_usuario as repo

app = Flask(__name__)
repositorio_usuario = repo.RepositorioUsuario()
crear_usuario = use_case.CrearUsuario(repositorio_usuario)

@app.route('/usuarios', methods=['POST'])
def crear_usuario_endpoint():
    data = request.json
    nombre = data.get('nombre')
    correo = data.get('correo')
    contraseña = data.get('contraseña')

    if not nombre or not correo or not contraseña:
        return jsonify({'mensaje': 'Todos los campos son obligatorios'}), 400

    usuario_nuevo = crear_usuario.ejecutar(nombre, correo, contraseña)

    return jsonify({
        'id': usuario_nuevo.id,
        'nombre': usuario_nuevo.nombre,
        'correo': usuario_nuevo.correo
    }), 201

if __name__ == '__main__':
    app.run(debug=True)