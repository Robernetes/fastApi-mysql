from sqlalchemy import Column, Integer, String, Table
from config.db import meta, engine

users = Table('users',meta, Column('id',Integer,primary_key=True),Column('name',String(50)),Column('email',String(50)),Column('password',String(150)))

meta.create_all(engine)