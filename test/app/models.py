from app import db


class Bar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    

    def __repr__(self):
        return '<Bar %r>' % (self.name)



