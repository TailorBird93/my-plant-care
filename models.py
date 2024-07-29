from myplantcare import db

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    watering = db.Column(db.String(50), nullable=False)
    environment = db.Column(db.String(20), nullable=False)
    care_level = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Plant {self.name}>'