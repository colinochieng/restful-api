# from marshmallow import Schema, fields, EXCLUDE, INCLUDE, RAISE


# class UserSchema(Schema):
#     name = fields.String(required=True)
#     email = fields.Email(required=True)

#     class Meta:
#         unknown = EXCLUDE


# input_data = {
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "age": 30,
#     "address": "123 Main St",
# }

# user_schema = UserSchema()
# result = user_schema.load(input_data)
# print(result)

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Setup the database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

try:
    user = User(name='John Doe', email='john.doe@example.com', age=30)  # 'age' is not a defined attribute
    session.add(user)
    session.commit()
except TypeError as e:
    print(f"Error: {e}")
