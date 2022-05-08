from project import db

class Club(db.Model):

    __tablename__ = 'clubs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    description = db.Column(db.String(500))

    # initialise an instance (row) of a table/entity
    def __init__(self, name, description):
        self.name = name
        self.description = description


    # __repr__ is used to represent an instance, such as for print() function
    def __repr__(self):
        return f"Name: {self.name}"

db.create_all()
