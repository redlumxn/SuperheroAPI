"""
This creates a Restful server that servers the SuperHeroes API
"""
import json
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from flask import abort

app = Flask(__name__)
api = Api(app)

def readSuperheroes():
    """
    This function reads the content of the 'superheroes.json' and return it as a JSON obj
    """
    f = open('./data/superheroes.json')
    superheores = json.load(f)
    f.close()
    return superheores

def searchSuperhero(name, superheroes):
    """
    This function search for the given superhero name in the given superhero list
    name: string rpresents the superhero name
    superheroes: list of JSON objects
    """
    try:
        result = next(sh for sh in superheroes if sh['superheroName'].lower()==name.lower())
    except StopIteration:
        abort(400,'Superhero not found in our database, try calling /api/v1/superheroes to get all of our registered heroes')
    return result

class Superhero(Resource):
    """
    Serves the /api/v1/superhero/<name> path
    """
    def get(self, name):
        superheroes = readSuperheroes()
        return searchSuperhero(name,superheroes)


class Superheroes(Resource):
    """
    Serves the /api/v1/superheroes path
    """
    def get(self):
        return readSuperheroes()

api.add_resource(Superhero, '/api/v1/superhero/<name>') # get a specific hero        
api.add_resource(Superheroes, '/api/v1/superheroes') # get all heroes


if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5002')