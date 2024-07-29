from flask import render_template, request, redirect, url_for
from . import app, db
from .models import Plant

@app.route('/')
def index():
    plants = Plant.query.all()
    return render_template('index.html', plants=plants)

@app.route('/add', methods=['GET', 'POST'])
def add_plant():
    if request.method == 'POST':
        name = request.form['name']
        watering = request.form['watering']
        environment = request.form['environment']
        fruit = request.form.get('fruit') == 'on'
        care_level = request.form['care_level']
        new_plant = Plant(name=name, watering=watering, environment=environment, fruit=fruit, care_level=care_level)
        db.session.add(new_plant)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_plant.html')

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

@app.route('/delete/<int:id>')
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/view/<int:id>')
def view_plant(id):
    plant = Plant.query.get_or_404(id)
    return render_template('view_plant.html', plant=plant)