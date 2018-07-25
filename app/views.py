from flask import  Flask,jsonify,make_response
from flask_restful import Resource,Api,reqparse
import json
from app.model.models import EntryModel

entries_list = []


class Entries(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        """collecting args"""
        parser.add_argument('id', type=int, required=True)
        parser.add_argument('title', type=str,required=True)
        parser.add_argument('content', type=str,required=True)
        parser.add_argument('date', type=str, required=True)

        """getting specific args"""
        args = parser.parse_args()
        id = args['id']
        title = args['title']
        content=args['content']
        date=args['date']

        """creating an object"""
        entryobject = EntryModel(id,title,content,date)

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


    def get (self):
        return {'entries': entries_list} ,200;


class SingleEntry(Resource):

    def get(self,entryId):

        for entry in entries_list:
            if int(entryId) == int (entry['id']):
                final_data = {
                    'id' : entry['id'],
                    'title':entry['title'],
                    'content':entry['content'],
                    'date':entry['date']
                }
                return {'entry': final_data}, 200

        return make_response(jsonify({
            'message':'Sorry the entry does not exist'
        }),404)

    def put(self, entryId):

        parser = reqparse.RequestParser()
        """collecting args"""
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('content', type=str, required=True)
        parser.add_argument('date', type=str, required=True)

        """getting specific args"""
        args = parser.parse_args()

        title = args['title']
        content = args['content']
        date = args['date']

        for entered_entry in entries_list:
            if int(entryId) == int(entered_entry['id']):
                """assign new entry"""
                entered_entry['title'] = title
                entered_entry['content'] = content
                entered_entry['date'] = date

                """enter updated entry in a dictionary """

                final_data = {
                    'id': entered_entry['id'],
                    'title': entered_entry['title'],
                    'content': entered_entry['content'],
                    'date': entered_entry['date']
                }

                return make_response(jsonify({
                    'message': 'entry updated successfully',
                    'entry': final_data
                }), 200)
            return make_response(jsonify({
                'message': 'entry not found please'
            }), 404)


