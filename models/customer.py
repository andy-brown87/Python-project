from app import db

class Customer(db.Model):
    __tablename__ = "customers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    phone_number = db.Column(db.Integer)
    address = db.Column(db.String(64))

    def __repr__(self):
        return f"<Customer: {self.id}: {self.name}>"