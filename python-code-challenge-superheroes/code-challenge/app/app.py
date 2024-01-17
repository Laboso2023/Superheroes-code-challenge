#!/usr/bin/env python3

from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from test import all_names 

from models import db, Hero
import os
abs_path = os.getcwd()
db_path = f'{abs_path}/db/app.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'This is the home page. Please use the /api/heroes endpoint to get and post heroes.'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    if request.method == 'GET':
        return jsonify(all_names)
    else:
        return make_response('Method not allowed', 405)
    

if __name__ == '__main__':
    app.run(port=3000 , debug=True)
