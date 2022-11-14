from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://64.media.tumblr.com/58ad30500e096781e56e5f31e50c561c/0767393739a2484f-05/s540x810/2bfbc14411783260ef0d80c4cafd99a55a12aca1.pnj"

db = SQLAlchemy()


class Pet(db.Model):
    """Pet Database"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Submitted image or default image"""

        return self.photo_url or DEFAULT_IMAGE


def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)