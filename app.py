from flask import Flask, render_template
from rethinkdb import r
app = Flask(__name__)



@app.route('/')
def home():
    r.connect('localhost', 28015).repl()
    datos = list(r.db("reservaciones").table("asientos").run()) 

    return render_template("home.html", data=datos)

@app.route('/3d')
def res3d():
    r.connect('localhost', 28015).repl()
    datos = list(r.db("reservaciones").table("asientos").run()) 

    return render_template("3d.html", data=datos)