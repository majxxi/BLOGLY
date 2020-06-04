"""Blogly application."""

from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'imsocool'

app.debug = True
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def redirect_to_users():
    """ Redirects to the list of users. """

    return redirect('/users')


@app.route('/users')
def show_index():
    """ Show all users list and link to add-user """
    
    users = User.query.all()
    
    return render_template('users_list.html', users=users)


@app.route('/users/new')
def show_create_page():
    """ Show the new user creation form """

    return render_template('user_form.html')


@app.route('/users/new', methods=["POST"])
def handle_new_user():
    """ Obtain Form info and place into database """

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:id>')
def show_user_profile(id):
    """ Return the user's profile page """
    
    user = User.query.get(id)
    return render_template('user_profile.html', user=user)


@app.route('/users/<int:id>/edit')
def show_edit_page(id):
    """ Display the edit page for selected user """

    return render_template('edit_page.html', id=id)

@app.route('/users/<int:id>/edit', methods=["POST"])
def handle_edit(id):
    """ Obtain Form info and update the database """
    user = User.query.get(id)
    
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:id>/delete', methods=["POST"])
def delete_user(id):
    """ Delete the user by id from the database and redirect
        to the users list """

    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')
