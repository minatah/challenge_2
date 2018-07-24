import uuid
import json


class EntryModel:
    def __init__(self, title, content, date):
        self.id = uuid.uuid4().int
        self.title_ = title
        self.content_ = content
        self.date_ = date

    def myjson(self):
        return json.dumps({
            'id': self.id,
            'title': self.title_,
            'content': self.content_,
            'date': self.date_

        })