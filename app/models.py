from app import db
from datetime import date 


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40), nullable=False)
    lname = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(6))
    email = db.Column(db.String(40))
    location = db.Column(db.String(40))
    bio = db.Column(db.String(200))
    image = db.Column(db.String(100)) # stores the name of the image file to be rendered
    date_created = db.Column(db.Date())

    def __init__(self, fname, lname, gender, email, location, bio, image):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.image = image
        self.date_created = date.today()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<ID {0}\nUser {1} {2}>'.format(self.id, self.fname, self.lname)