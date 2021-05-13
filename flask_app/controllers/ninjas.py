from flask_app.models.dojo import Dojo
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def show_create_ninja():
    return render_template("create_ninja.html", all_dojos = Dojo.get_all())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')