from flask_login import UserMixin
from flask import url_for

class UserLogin(UserMixin):
    def fromDB(self, user_id, db):
        self.__user = db.get_user(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user['id'])

    def get_username(self):
        return self.__user['username'] if self.__user else "Без логина"
    
    def get_firstname(self):
        return self.__user['first_name'] if self.__user else "Без имени"
    
    def get_lastname(self):
        return self.__user['last_name'] if self.__user else "Без фамилии"

    def get_email(self):
        return self.__user['email'] if self.__user else "Без email"
    
    def get_registrationdate(self):
        return str(self.__user['registration_date'])

    def get_avatar(self, app):
        img = None
        if not self.__user['avatar']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='images/default.png'), "rb") as f:
                    img = f.read()
            except FileNotFoundError as e:
                print("Не найден аватар по умолчанию: " + str(e))
        else:
            img = self.__user['avatar']

        return img

    def verify_ext(self, filename):
        ext = filename.rsplit('.', 1)[1]
        if ext == "png" or ext == "PNG":
            return True
        return False