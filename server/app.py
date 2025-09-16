#!/usr/bin/env python3

from flask import Flask, make_response

app = Flask(__name__)
app.json.compact = False

# Sample data
pets_data = [
    {'id': 1, 'name': 'Fido', 'species': 'Dog'},
    {'id': 2, 'name': 'Whiskers', 'species': 'Cat'},
    {'id': 3, 'name': 'Buddy', 'species': 'Dog'},
    {'id': 4, 'name': 'Tweety', 'species': 'Bird'},
    {'id': 5, 'name': 'Nemo', 'species': 'Fish'}
]

@app.route('/')
def index():
    body = {'message': 'Welcome to the pet directory!'}
    return make_response(body, 200)

@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = next((p for p in pets_data if p['id'] == id), None)
    
    if pet:
        body = {'id': pet['id'],
                'name': pet['name'],
                'species': pet['species']}
        status = 200
    else:
        body = {'message': f'Pet {id} not found.'}
        status = 404

    return make_response(body, status)

@app.route('/species/<string:species>')
def pet_by_species(species):
    pets = []
    for pet in pets_data:
        if pet['species'].lower() == species.lower():
            pet_dict = {'id': pet['id'],
                        'name': pet['name']}
            pets.append(pet_dict)
    
    body = {'count': len(pets),
            'pets': pets}
    return make_response(body, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
