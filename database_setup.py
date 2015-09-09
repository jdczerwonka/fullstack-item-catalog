from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Activity(Base):
    __tablename__ = 'activity'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

##    @property
##    def serialize(self):
##       """Return object data in easily serializeable format"""
##       return {
##           'name'         : self.name,
##           'id'           : self.id,
##       }
 
class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    description = Column(String(250))
    activity_id = Column(Integer,ForeignKey('activity.id'))
    activity = relationship(Activity)


##    @property
##    def serialize(self):
##       """Return object data in easily serializeable format"""
##       return {
##           'name'         : self.name,
##           'description'         : self.description,
##           'id'         : self.id,
##           'price'         : self.price,
##           'course'         : self.course,
##       }



engine = create_engine('sqlite:///itemcatalog.db')
 

Base.metadata.create_all(engine)
