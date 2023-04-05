from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    phone_number = db.Column(db.Integer)

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Must enter a name')
        return name
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError('Phone number error')
        return phone_number


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)

    @validates('content')
    def validate_content(self, key, content):
        if not len(content) >= 250:
            raise ValueError('Content Length Error')
        return content
    @validates('summary')
    def validate_summary(self, key, summary):
        if not len(summary) <= 250:
            raise ValueError('Summary Error')
        return summary
    @validates('category')
    def validate_category(self, key, category):
        if category == 'Fiction' or 'Non-Fiction':
            raise ValueError('Incorrect Category Type')
        return category

