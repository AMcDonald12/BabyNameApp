from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

class AllNames(Resource):
    def get(self):
        file = open('../WebScraping/babynames.json')
        names = json.load(file)
        return {'NAMES' : names}, 200

api.add_resource(AllNames, '/')

if __name__ == '__main__':
    app.run() 