from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class Favourite_Countries(base):
    __tablename__ = "Favourite_Countries"
    Id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer, primary_key=False)
    cuisine = Column(String)
    continent = Column(String)
    capital_city = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above


session = Session()


# creating the database using declarative_base subclass
base.metadata.create_all(db)


jamaica = Favourite_Countries(
    name = "Jamaica",
    population = 2000000,
    cuisine = "Ackee and Saltfish",
    continent = "North America",
    capital_city = "Kingston"
)


session.add(jamaica)


session.commit()

countries = session.query(Favourite_Countries)
for country in countries:
    print(country.name, country.population, country.cuisine, country.continent, country.capital_city, sep=" | ")