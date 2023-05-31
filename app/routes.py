from app import app
from flask import Flask, render_template

@app.route("/")
def index():
    return render_template('main_page.html')

@app.route("/name",defaults={'name' :"Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"

@app.route("/o_autorze")
def author():
    return render_template('about_author.html')

@app.route("/ekstrakcja")
def extraction():
    return render_template('extraction.html')

@app.route("/lista_produktow")
def productList():
    return render_template('product_list.html')