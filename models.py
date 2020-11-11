from settings import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    profile_image = db.Column(db.String(120))
    access_token = db.Column(db.String(120), unique=True)
    sid = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, login, name, email, profile_image, access_token, sid):
        self.login = login
        self.name = name
        self.email = email
        self.profile_image = profile_image
        self.access_token = access_token
        self.sid = sid
        
    def __repr__(self):
        return str({
            'login': self.login,
            'name': self.name,
            'email': self.email,
            'profile_image': self.profile_image,
            'access_token': self.access_token,
            'sid': self.sid
        })

