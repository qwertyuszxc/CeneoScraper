from app import app
from flask import Flask, render_template, request, redirect, url_form

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/name",defaults={'name' :"Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"

@app.route("/o_autorze") 
def author():
    return render_template('about_author.html')

@app.route("/ekstrakcja", method =['POST','GET'])
def extraction():
    if request.method == 'POST':
        product_code = request.form.get['product_id']
        
        return redirect(url_for{'product',product_code=product_id})
    return render_template('extraction.html')

@app.route("/ekstrakcja/<product_code>")
def extraction(product_code):
    return render_temlate(extraction.html)   

@app.route("/lista_produktow")
def productList():
    return render_template('product_list.html')
    