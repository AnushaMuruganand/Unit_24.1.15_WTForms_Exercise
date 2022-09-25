from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE ="https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

# MODELS GO BELOW!

class Pet(db.Model):
    """ PET MODEL """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = False, default = DEFAULT_IMAGE)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def image_url(self):
        """Return image for pet -- if present else return "DEFAULT_IMAGE" variable's value."""

        return self.photo_url or DEFAULT_IMAGE