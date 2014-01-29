"""
Appium Demo
http://www.youtube.com/watch?v=eKhuF_4KzYo

http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html
http://docs.sqlalchemy.org/en/rel_0_8/orm/query.html

join: q = session.query(User).join(Address, User.id==Address.user_id)

---
q = session.query(Address).select_from(User).\
                join(User.addresses).\
                filter(User.name == 'ed')

equivalent:
SELECT address.* FROM user
    JOIN address ON user.id=address.user_id
    WHERE user.name = :name_1


"""

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
        def __repr__(self):
            return "<User(name='%s')>" % (self.name)

    Base.metadata.create_all(engine)

def ses():
    Base = declarative_base()
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String(255))
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return "<User(name='%s')>" % (self.name)

    Session = sessionmaker(bind=engine)
    session = Session()
    user_john = User(name='john')
    session.add(user_john)
    session.commit()

def q():
    Base = declarative_base()
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String(255))
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return "<User(name='%s')>" % (self.name)
 
    Session = sessionmaker(bind=engine)
    session = Session()
    #user_john = User(name='john')
    #print user_john in session
    #x = session.query(User).filter_by(id = 1)
    #print x.id

    #for user in session.query(User).filter(User.id==5):
    #    print user
    # return None if found nothing
    print session.query(User).filter(User.id==5).first()
    print session.query(User).get(3)
#create() # works
#ses() # works
#ses()
q()