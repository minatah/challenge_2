from flask import Flask
from flask_restful import  Api
from app.entries.managentries import Entries

app = Flask(__name__)
app.secret_key = "aminah"

"""Am initializing an API for my application"""
api = Api(app)

api.add_resource(Entries,'/api/v1/entries')