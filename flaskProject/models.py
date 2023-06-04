from config import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)


class Customer(db.Model):
    __tablename__ = 'Customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(60), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sex': self.sex,
            'phone': self.phone,
            'address': self.address
        }


class Supplier(db.Model):
    __tablename__ = 'Supplier'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact_person = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact_person': self.contact_person,
            'phone': self.phone,
            'address': self.address
        }


class Medicine(db.Model):
    __tablename__ = 'Medicine'
    id = db.Column(db.String(40), primary_key=True, nullable=False, unique=True)
    storage_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    s_id = db.Column(db.Integer, db.ForeignKey('Supplier.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(60), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'storage_id': self.storage_id,
            's_id': self.s_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'description': self.description
        }


class Orderlist(db.Model):
    __tablename__ = 'Orderlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    m_id = db.Column(db.String(40), db.ForeignKey('Medicine.id'))
    c_id = db.Column(db.Integer, db.ForeignKey('Customer.id'))
    name = db.Column(db.String(100))
    type = db.Column(db.String(20), nullable=False, default="销售")
    date = db.Column(db.Date)
    quantity = db.Column(db.Integer, nullable=False)
    is_returned = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'm_id': self.m_id,
            'c_id': self.c_id,
            'name': self.name,
            'type': self.type,
            'date': self.date,
            'quantity': self.quantity,
            'is_returned': self.is_returned
        }


class Purchase(db.Model):
    __tablename__ = 'Purchase'
    id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    type = db.Column(db.String(20), nullable=False, default="采购")
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    medicine_id = db.Column(db.String(40), db.ForeignKey('Medicine.id'), nullable=False)
    medicine = db.relationship('Medicine', backref=db.backref('purchases', lazy=True))
    is_returned = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'purchase_date': self.purchase_date,
            'quantity': self.quantity,
            'type': self.type,
            'price': self.price,
            'medicine_id': self.medicine_id,
            'is_returned': self.is_returned
        }
