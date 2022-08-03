from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)



# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above


session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# ada_lovelace = Programmer(
#     first_name = "Ada",
#     last_name = "Lovelace",
#     gender = "F",
#     nationality = "British",
#     famous_for = "First Programmer"
# )


# alan_turing = Programmer(
#     first_name = "Alan",
#     last_name = "Turing",
#     gender = "M",
#     nationality = "British",
#     famous_for = "Modern Computing"
# )


# grace_hopper = Programmer(
#     first_name = "Grace",
#     last_name = "Hopper",
#     gender = "F",
#     nationality = "American",
#     famous_for = "COBOL"

# )


# margaret_hamilton = Programmer(
#     first_name = "Margaret",
#     last_name = "Hamilton",
#     gender = "F",
#     nationality = "American",
#     famous_for = "Apollo 11"
# )


# bill_gates = Programmer(
#     first_name = "Bill",
#     last_name = "Gates",
#     gender = "M",
#     nationality = "American",
#     famous_for = "Microsoft Founder"

# )


# tim_berners_lee = Programmer(
#     first_name = "Tim",
#     last_name = "Berneres-Lee",
#     gender = "M",
#     nationality = "British",
#     famous_for = "Creator of WWW"
# )


# jacob_peat = Programmer(
#     first_name = "Jacob",
#     last_name = "Peat",
#     gender = "M",
#     nationality = "British",
#     famous_for = "Overachieving"
# )

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(jacob_peat)

#updating a single record
# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.nationality = "Jamaican"

#updating multiple records
# gender_update = session.query(Programmer)
# for person in gender_update:
#     if person.gender == "F":
#          person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
# session.commit()

fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

if programmer is not None:
    print("Programmer Found ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this user? y/n")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else:
        print("Programmer not deleted")
else:
    print("No records found")    

    
        
programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.id, programmer.first_name, programmer.gender, programmer.nationality, programmer.famous_for, sep=" | ")