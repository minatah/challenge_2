from flask import  Flask,jsonify,make_response
from flask_restful import Resource,Api,reqparse
import json
from app.model.entrymodel import EntryModel

entries_list = []

class Entries(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        """collecting args"""
        parser.add_argument('title', type=str,required=True)
        parser.add_argument('content', type=str,required=True)
        parser.add_argument('date', type=str, required=True)

        """getting specific args"""
        args = parser.parse_args()
        title = args['title']
        content=args['content']
        date=args['date']

        """creating an object"""
        entryobject = EntryModel(title,content,date)

        """converting the object data to JSON format """
        convert_obj_data = json.loads(entryobject.myjson())

        """checking if there are duplicates """

        for entered_entry in entries_list:
            if str(title).strip() == str(entered_entry['title']).strip():
                return make_response(jsonify({
                    'message': 'This entry already exists.'
                }), 409)

        """inserting data in a list"""
        entries_list.append(convert_obj_data)



        return make_response(jsonify({
            'message':'Created an entry successfully.'
        }),201)

