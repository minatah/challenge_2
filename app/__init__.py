from flask import Flask
from flask_restful import  Api
from app.entries.views import Entries,SingleEntry

app = Flask(__name__)
app.secret_key = "aminah"

"""Am initializing an API for my application"""
api = Api(app)

api.add_resource(Entries,'/api/v1/entries')
api.add_resource(SingleEntry,'/api/v1/entries/<entryId>')