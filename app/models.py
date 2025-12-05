from app import db
from datetime import datetime, timezone


class Client(db.Model):
    __tablename__ = "Client"

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255), nullable=False)
    client_company = db.Column(db.String(255), nullable=False)
    client_location = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False, unique=True)
    contact_email = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)
    deleted_at = db.Column(db.DateTime, default=None, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "client_name": self.client_name,
            "client_company": self.client_company,
            "client_location": self.client_location,
            "contact_person": self.contact_person,
            "contact_number": self.contact_number,
            "contact_email": self.contact_email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at
        }