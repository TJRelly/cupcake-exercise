"""Flask app for Cupcakes"""

from flask import Flask, jsonify, render_template, redirect, flash, request
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Cupcake

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "scrumdidlyumptious"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def get_home_page():
    """Redirects to home page"""
    return redirect('/cupcakes')

@app.route('/cupcakes')
def get_cupcakes():
    """Shows all cupcakes"""
    cupcakes = db.session.query(Cupcake.flavor)
    
    return render_template('cupcakes.html', cupcakes=cupcakes)

@app.route('/api/cupcakes')
def get_api_cupcakes():
    """
    Returns JSON for all cupcakes
    {'cupcakes': [{id, flavor,...}, ...]}
    """
    cupcakes = Cupcake.query.all()
    cupcakes_dict = [c.serialize() for c in cupcakes]
          
    return jsonify(cupcakes=cupcakes_dict)

@app.route('/api/cupcakes/<cupcake_id>')
def get_one_cupcake(cupcake_id):
    """Returns JSON data for a single cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
          
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """
    Creates a cupcake 
    Responds with JSON 
    {cupcake: {id, flavor, size, rating, image}}
    """
    
    cupcake_data = {
        "flavor": request.json["flavor"],
        "size": request.json["size"],
        "rating": request.json["rating"],
        "image": request.json.get("image", "https://tinyurl.com/demo-cupcake")
    }
    
    new_cupcake = Cupcake(**cupcake_data)
    db.session.add(new_cupcake)
    db.session.commit()
          
    return (jsonify(new_cupcake=new_cupcake.serialize()), 201)