from app import app
from models import db, Pet
import random

names = ['Robin', 'Gwendolyn', 'Michael', 'Austin', 'Jennifer', 'Jenna', 'Crystal', 'Jacob', 'Nicole', 'Trevor']
species = ['Hamster', 'Dog', 'Turtle', 'Cat', 'Chicken']

with app.app_context():
    Pet.query.delete()
    
    for i in range(10):
        pet = Pet(
            name=random.choice(names),
            species=random.choice(species)
        )
        db.session.add(pet)
    
    db.session.commit()
    print("Database seeded with 10 pets!")