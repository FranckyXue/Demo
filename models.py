from extensions import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(10))

    @property
    def serialize(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'gender': self.gender
        }
