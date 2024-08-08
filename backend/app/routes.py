from flask import render_template, url_for, flash, redirect, current_app as app
#from app.forms import CharCreateForm

@app.route("/")
@app.route("/home", methods=['GET'])
def home():
    #return render_template('home.html')
    return {"title" : "D&D Application", "body": "Hello!"}

@app.route("/about")
def about():
    return render_template('about.html')

""" @app.route("/char-create", methods=['GET', 'POST'])
def charcreate():
    form = CharCreateForm()
    if form.validate_on_submit():
        flash(f'Created Chracter!', 'success')
        return redirect(url_for('created'))
    return render_template('charcreate.html', title='Create Character', form=form) """

@app.route("/random-char")
def randomchar():
    return render_template('randomchar.html')

@app.route("/created")
def created():
    return render_template('created.html')