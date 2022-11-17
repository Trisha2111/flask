from flask import Flask, render_template

app=Flask(__name__)

@app.route("/father")
def index():
    return "My Father Name is Mukesh Malani"

@app.route("/mother")
def index1():
    return "My name is Shweta Malani"

@app.route("/flask1")
def index2():
    return render_template("main.html",name="TRISHA",age="13")

app.run()

