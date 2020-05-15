import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


DATABASE_URL='postgres://nestor:P35cad0-@zu1@localhost:5432/lecture3'


engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f'{flight.origin} to {flight.destination}, {flight.duration} minutes.')

if __name__ == '__main__':
    main()
