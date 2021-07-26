from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:password_here@localhost:3306/db_name')

meta = MetaData()

db_conn = engine.connect()