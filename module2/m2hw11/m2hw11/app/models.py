from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    contact_name = db.Column(db.String(32), index = True, unique = True)
    phone = db.Column(db.String(32), index = True, unique = True)
    mail = db.Column(db.String(32), index = True, unique = True)
    address = db.Column(db.String(128))
    birthday = db.Column(db.String(10), index = True)
    
    def __repr__(self):
        return f'Contact {self.contact_name}'