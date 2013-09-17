
from promlib import db

books = db.Table('books',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    books = db.relationship('Book', secondary=books,
        backref=db.backref('authors', lazy='dynamic'))

    def __repr__(self):
        return '<Author %r>' % (self.name)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))

    def __repr__(self):
        return '<Book %r>' % (self.title)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))  # hash actually

    def __repr__(self):
        return '<User %r>' % (self.username)

