from flask import Flask, render_template

from . import app

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/testing_app1/addEquipment')
def addEquipment():
    return render_template('testing_app1/addEquipment.html')

@app.route('/testing_app1/equipment')
def equipment():
    return render_template('testing_app1/equipment.html')

@app.route('/testing_app1/equipmentList')
def equipmentList():
    return render_template('testing_app1/equipmentList.html')

# @app.route('/testing_app1/addEquipment')
# def addEquipment():
#     return render_template('testing_app1/addEquipment.html')
#
# @app.route('/testing_app1/addEquipment')
# def addEquipment():
#     return render_template('testing_app1/addEquipment.html')

