"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app): 
    """ Connect to database. """

    db.app = app
    db.init_app(app)


class User(db.Model):

    __tablename__: 'User'

    def __repr__(self):
        """ Show info about pet. """
        user = self
        print(f"<User {user.first_name}, {user.last_name}, {user.id}, {user.image_url}>")

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    image_url = db.Column(db.String, nullable = False, default = 'No image')

    def get_full_name(self):

        return f"{self.first_name} {self.last_name}"

    posts = db.relationship('Post', backref='user')


class Post(db.Model):

    def __repr__(self):

        post = self
        print(f"<Post {post.post_id}, {post.title}, {post.created_at}, {post.user_id} >")

    __tablename__: 'posts'

    post_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(21), nullable = False)
    content = db.Column(db.String(500), nullable = True)
    created_at = db.Column(db.DateTime, nullable = False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')
