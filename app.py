from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Plant

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