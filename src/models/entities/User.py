from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname="", joined_date=None):
        self.id =id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.joined_date = joined_date
     
    @classmethod
    def check_password(self, hashed_password,password):
        return check_password_hash(hashed_password, password)