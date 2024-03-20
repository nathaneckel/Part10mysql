# db template code
import sqlalchemy as db
import mysqlclient
# mysqlclient (a maintained fork of MySQL-Python)
engine = db.create_engine("mysql+mysqldb://nathan2:Coal@localhost/data5zero")

conn = engine.connect()
metadata = db.MetaData()  #create a new metaData object, used below in table, Person CLASS

Person = db.Table('Person', metadata,
              db.Column('Id', db.Integer(),primary_key=True),
              db.Column('FirstName', db.String(255), default=''),
              db.Column('LastName', db.String(255), default=''),
              )

metadata.create_all(engine) #person class/table goes in here.  Object/Relational MAPPER

query = db.insert(Person).values(Id=101, FirstName ='Andrew', LastName='Johnson') #query Object that does an INSERT on the db

Result = conn.execute(query) #insert this record into the database

output = conn.execute(Person.select()).fetchall() #create & execute a new query and modify w/fetchall
print(output)