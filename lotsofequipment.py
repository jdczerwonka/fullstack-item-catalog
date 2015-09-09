from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Activity, Base, Equipment

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Equipment for Soccer
activity1 = Activity(name="Soccer")

session.add(activity1)
session.commit()

equipment1 = Equipment(name="shinguards", description="Pads that protect the players shins and ankles",
                     activity=activity1)

session.add(equipment1)
session.commit()


equipment2 = Equipment(name="cleats", description="Allows the player to grip the grass to aid in sprinting and turning.",
                     activity=activity1)

session.add(equipment2)
session.commit()

equipment3 = Equipment(name="soccer ball", description="A [multi]colored ball in the shape of a sphere",
                     activity=activity1)

session.add(equipment3)
session.commit()

equipment4 = Equipment(name="goal", description="An opening in which a player attempts to kick the soccer ball into to score.",
                     activity=activity1)

session.add(equipment4)
session.commit()


# Equipment for Basketball
activity2 = Activity(name="Basketball")

session.add(activity2)
session.commit()

equipment1 = Equipment(name="basketball", description="An orange ball in the shape of a sphere",
                     activity=activity2)

session.add(equipment1)
session.commit()

equipment2 = Equipment(name="hoop", description="A hoop ten feet off the ground with a square backboard in which the player shoots into.",
                     activity=activity2)

session.add(equipment2)
session.commit()

# Equipment for Baseball
activity1 = Activity(name="Baseball")

session.add(activity1)
session.commit()

# Equipment for Frisbee
activity1 = Activity(name="Frisbee")

session.add(activity1)
session.commit()

# Equipment for Snowboarding
activity1 = Activity(name="Snowboarding")

session.add(activity1)
session.commit()

# Equipment for Rock Climbing
activity1 = Activity(name="Rock Climbing")

session.add(activity1)
session.commit()

# Equipment for Hockey
activity1 = Activity(name="Hockey")

session.add(activity1)
session.commit()



print "added equipment!"
