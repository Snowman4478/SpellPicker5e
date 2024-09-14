from flask import render_template, url_for, flash, redirect, request, current_app as app
from app import db
from .spells_logic import generate_spells

@app.route("/")
@app.route("/home", methods=['GET'])
def home():
    #return render_template('home.html')
    return {"title" : "D&D Application", "body": "Hello!"}

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/spell-picker", methods=['POST'])
def spell_picker():
    return render_template('spell_picker.html')

@app.route("/spell-picker/process", methods=['POST'])
def spell_picker_process():
    data = request.get_json()
    class_type = data.get('class_type')
    level = data.get('level')
    school = data.get('school', None)
    damage_type = data.get('damage_type', None)

    generated_spells = generate_spells(class_type, level, damage_type, school)

    return generated_spells
