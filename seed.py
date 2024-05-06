"""Seed file to make sample data for db."""

from models import db, Cupcake

# Create all tables
db.drop_all()
db.create_all()

CUPCAKES = [
    {
        "flavor": "chocolate",
        "size": "small",
        "rating": 6,
        "image": "https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    },
    {
        "flavor": "vanilla",
        "size": "medium",
        "rating": 7,
        "image": "https://cdn.bakedbyrachel.com/wp-content/uploads/2015/07/whitecupcakes_bakedbyrachel-1-1024x1536.jpg"
    },
    {
        "flavor": "strawberry",
        "size": "large",
        "rating": 9,
        "image": "https://cdn.bakedbyrachel.com/wp-content/uploads/2016/05/strawberrylemonadecupcakes_bakedbyrachel-2.jpg"
    },
    {
        "flavor": "blue velvet",
        "size": "medium",
        "rating": 10,
        "image": "https://jennifermeyering.com/wp-content/uploads/2018/02/blue-velvet-cupcakes-1.jpg"
    },
    {
        "flavor": "lemon",
        "size": "small",
        "rating": 9,
        "image": "https://cdn.bakedbyrachel.com/wp-content/uploads/2018/05/lemoncupcakesccfrosting_bakedbyrachel-3-1024x1536.jpg"
    },
    {
        "flavor": "banana",
        "size": "large",
        "rating": 8
    },
    {
        "flavor": "coconut",
        "size": "medium",
        "rating": 9
    },
    {
        "flavor": "caramel",
        "size": "small",
        "rating": 8,
        "image": "https://cdn.bakedbyrachel.com/wp-content/uploads/2016/09/caramelapplebuttercupcakes_bakedbyrachel-4-1024x1536.jpg"
    },
    {
        "flavor": "pistachio",
        "size": "large",
        "rating": 5
    }
]

for cupcake_data in CUPCAKES:
    cupcake = Cupcake(**cupcake_data)
    db.session.add(cupcake)

db.session.commit()
