from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


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


class Medicine(db.Model):
    __tablename__ = 'Medicine'
    id = db.Column(db.String(40), primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(60), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'description': self.description
        }


class Orderlist(db.Model):
    __tablename__ = 'Orderlist'
    id = db.Column(db.Integer, primary_key=True)
    m_id = db.Column(db.String(40), db.ForeignKey('Medicine.id', ondelete='CASCADE'))
    c_id = db.Column(db.Integer, db.ForeignKey('Customer.id', ondelete='CASCADE'))
    type = db.Column(db.String(20))
    name = db.Column(db.String(100))
    date = db.Column(db.Date)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'm_id': self.m_id,
            'c_id': self.c_id,
            'type': self.type,
            'name': self.name,
            'date': self.date,
            'quantity': self.quantity
        }

