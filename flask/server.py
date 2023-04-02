from flask import Flask
from flask_restful import Resource, Api
import json
import random

app = Flask(__name__)
api = Api(app)

#Endpoints
class AllNames(Resource):
    def get(self):
        file = open('../WebScraping/babynames.json')
        names = json.load(file)
        return names, 200
    
class RandomName(Resource):
    def get(self):
        file = open('../WebScraping/babynames.json')
        names = json.load(file)
        gender = random.choice(list(names.keys()))
        letter = random.choice(list(names[gender].keys()))
        randomName = random.choice(names[gender][letter])
        return {'Name':randomName,'Gender':gender}, 200
      
#Paths
api.add_resource(AllNames, '/')
api.add_resource(RandomName, '/random')

if __name__ == '__main__':
    app.run(debug=True) 