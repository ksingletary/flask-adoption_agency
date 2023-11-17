from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet Model for PSQL"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, nullable=False, default=None)

    age = db.Column(db.Integer, nullable=False)

    notes = db.Column(db.String(100), nullable=False)
    
    available = db.Column(db.Boolean, nullable=False, default=True)




    