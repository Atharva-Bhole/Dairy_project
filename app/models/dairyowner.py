from . import db
from flask import current_app as app
from .farmer import farmers
from .muster_data import muster

class dairy_owner(db.Model):
    __tablename__ = 'dairy_owner'
    dairy_id = db.Column(db.Integer(), primary_key = True)
    dairy_name = db.Column(db.String())
    state = db.Column(db.String())
    taluka = db.Column(db.String())
    district = db.Column(db.String())
    village = db.Column(db.String())
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    farmers = db.relationship('farmers', backref='dairy_owner', lazy=True)
    muster = db.relationship('muster', backref='dairy_owner', lazy=True)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    def __repr__(self):
        return f"Dairy Name {self.dairy_name}, Dairy Id {self.dairy_id}"
