from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

#Endpoints
class Names(Resource):
    def get(self):
        file = open('../WebScraping/babynames.json')
        names = json.load(file)
        return {'NAMES' : names}, 200
  
#Paths
api.add_resource(Names, '/')

if __name__ == '__main__':
    app.run(debug=True) 