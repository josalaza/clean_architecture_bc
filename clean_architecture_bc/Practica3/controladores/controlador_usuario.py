from flask import Flask, request, jsonify
import clean_architecture_bc.Practica3.servicios.servicio_usuario as service
import clean_architecture_bc.Practica3.repositorios.repositorio_mysql as repository

app = Flask(__name__)
user_service = service.Servicio()
user_repository = repository.MySQLUserRepository(host="localhost", user="root", password="password", database="fluskdb")

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_repository, user_id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    else:
        return jsonify({'message': 'User not found'}), 404