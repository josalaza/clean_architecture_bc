class Servicio:
    def get_user(self, user_repository, user_id):
        return user_repository.find_by_id(user_id)