# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    
    sites= db.relationship('Site', backref='User' , lazy='dynamic')
    houses=db.relationship('House', backref='User' , lazy='dynamic')
    #is_admin = db.Column(db.Boolean, default=True)


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class House(db.Model):
    """
    Create a House table
    """

    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(60) ,index=True)
    house_num = db.Column(db.Integer , unique=True)
    area = db.Column(db.String(60) ,index=True)
    city = db.Column(db.String(60) ,index=True)
    room_cnt = db.Column(db.Integer ,index = True )
    bath_cnt = db.Column(db.Integer,index=True)
    amount = db.Column(db.Integer , index=True)
    balcony = db.Column(db.Integer , index=True)
    utility = db.Column(db.Integer , index=True)
    description = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return '<House: {}>'.format(self.name)
    
        
class Site(db.Model):
    """
    Create a Site table
    """

    __tablename__ = 'sites'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(60) ,index=True)
    site_num= db.Column(db.Integer , unique=True)
    area = db.Column(db.String(60) ,index=True)
    city = db.Column(db.String(60) ,index=True)
    sq_feet = db.Column(db.Integer, index=True)
    amount = db.Column(db.Integer , index=True)
    
    description = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    def __repr__(self):
        return '<Site: {}>'.format(self.name)

