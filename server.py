"""
This creates a Restful server that servers the SuperHeroes API
"""
import json
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

def read_superheroes():
    """
    This function reads the content of the 'superheroes.json' and return it as a JSON obj
    """
    data = open('./data/superheroes.json')
    superheores = json.load(data)
    data.close()
    return superheores

def search_superhero(name, superheroes):
    """
    This function search for the given superhero name in the given superhero list
    name: string rpresents the superhero name
    superheroes: list of JSON objects
    """
    try:
        result = next(sh for sh in superheroes if sh['superheroName'].lower() == name.lower())
    except StopIteration:
        abort(404, 'Superhero not found in our database,' \
                'try calling /api/v1/superheroes to get all of our registered heroes')
    return result

@app.route('/api/v1/superhero/<superhero>', methods=['POST'])
def add_superhero(superhero):
    """
    Serves the POST /api/v1/superhero/<name> path
    """
    content = request.json
    print(content)
    superheroes = read_superheroes()
    superheroes.append(content)
    data = open('./data/superheroes.json', 'w')
    data.write(json.dumps(superheroes))
    data.close()
    return 'Superhero was registered in our database'

@app.route('/api/v1/superhero/<name>', methods=['GET'])
def get_superhero(name):
    """
    Serves the GET /api/v1/superhero/<name> path
    """
    superheroes = read_superheroes()
    return jsonify(search_superhero(name, superheroes))

@app.route('/api/v1/superheroes', methods=['GET'])
def get_all_superheroes():
    """
    Serves the /api/v1/superheroes path
    """
    return jsonify(read_superheroes())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')
