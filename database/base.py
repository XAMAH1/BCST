from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mssql+pyodbc://DESKTOP-2NFCDE2/BCST?driver=ODBC Driver 11 for SQL Server')
engine = create_engine('mysql+pymysql://root:root@localhost:3306/bcst')

meta = MetaData()
session = sessionmaker(bind=engine)

autme_user = Table("autme_user", meta,
                   Column("id", Integer, primary_key=True),
                   Column("login", String(100), nullable=False),
                   Column("password", String(250), nullable=False),
                   Column("date_create", String(40)),
                   Column("IMEI", String(100))
                   )

user = Table("user", meta,
             Column("id", Integer, primary_key=True),
             Column("autme_id", Integer, nullable=False),
             Column("fio", String(150), nullable=False),
             Column("mail", String(100), nullable=False),
             Column("phone", String(25), nullable=False)
             )

math = Table("math", meta,
             Column("id", Integer, primary_key=True),
             Column("user_id", Integer, nullable=False),
             Column("name_command_one", String(50), nullable=False),
             Column("name_command_two", String(50), nullable=False),
             Column("chet_command_one", Integer, nullable=False),
             Column("chet_command_two", Integer, nullable=False)
             )

commnad_user = Table("commnad", meta,
             Column("id", Integer, primary_key=True),
             Column("user_id", Integer, nullable=False),
             Column("name", String(50), nullable=False),
             Column("date_Create", String(50), nullable=False),
             )

player_command = Table("player_commnad", meta,
             Column("id", Integer, primary_key=True),
             Column("command_id", Integer, nullable=False),
             Column("fio", String(50), nullable=False),
             Column("number", String(50), nullable=False),
             )
def base_connect():
    meta.create_all(engine)
    connect = engine.connect()
    print("base connect")
    return connect