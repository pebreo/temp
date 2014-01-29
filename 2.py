from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os.path import abspath, basename, dirname, join, normpath
THIS_DIR =  dirname(abspath(__file__))
SQLITE_FILE = 'sqlite:///{}/foo.db'.format(THIS_DIR)
print SQLITE_FILE
engine = create_engine(SQLITE_FILE, echo=True)

#metadata = BoundMetaData(db)



def create():
    Base = declarative_base()

    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String(255))
        def __init__(self, name):
            self.name = name

    Base.metadata.create_all(engine)

def ses():
    Base = declarative_base()
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String(255))
        def __init__(self, name):
            self.name = name
    Session = sessionmaker(bind=engine)
    session = Session()
    user_john = User(name='john')
    session.add(user_john)
    session.commit()
create() # works
ses() # works
#ses()