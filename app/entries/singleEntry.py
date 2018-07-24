from flask import Flask,make_response,jsonify
from flask_restful import Resource,Api,reqparse
import json
from flask_restful import Resource,Api,reqparse
from app.entries.managentries import entries_list


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

