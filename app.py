from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Plant

def create_tables():
    with app.app_context():
        db.create_all()

        
# Homepage for all user plants
@app.route('/')
def index():
    plants = Plant.query.all()
    return render_template('index.html', plants=plants)

# Add new plant
@app.route('/add', methods=['GET', 'POST'])
def add_plant():
    if request.method == 'POST':
        name = request.form['name']
        watering = request.form['watering']
        environment = request.form['environment']
        care_level = request.form['care_level']
        new_plant = Plant(name=name, watering=watering, environment=environment, care_level=care_level)
        db.session.add(new_plant)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_plant.html')

# Edit plant
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_plant(id):
    plant = Plant.query.get_or_404(id)
    if request.method == 'POST':
        plant.name = request.form['name']
        plant.watering = request.form['watering']
        plant.environment = request.form['environment']
        plant.fruit = request.form.get('fruit') == 'on'
        plant.care_level = request.form['care_level']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_plant.html', plant=plant)

# Delete plant 
@app.route('/delete/<int:id>')
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for('index'))

# View plant
@app.route('/view/<int:id>')
def view_plant(id):
    plant = Plant.query.get_or_404(id)
    return render_template('view_plant.html', plant=plant)


# test for flask error
if __name__ == '__main__':
    app.run(debug=True)