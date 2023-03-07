from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/menu/')
def menu():
    return render_template('menu.html')

@app.route('/food/')
def food():
    return render_template('food.html')

@app.route('/services/')
def services():
    return render_template('services.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

