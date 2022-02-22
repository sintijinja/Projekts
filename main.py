from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/page.html')
def page():
  return render_template("page.html")

@app.route('/receptes.html')
def receptes():
  return render_template("receptes.html")

@app.route('/rcp.html')
def rcp():
  return render_template("rcp.html")

app.run(host="0.0.0.0",port= 8080)