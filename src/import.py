import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# We create the conection to the database
DATABASE_URL = 'postgres://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))


def main():
    # We open the csv file with the data
    f = open('flights.csv')
    reader = csv.reader(f)

    # We save the data from the csv to the database
    for origin, destination, duration in reader:
        db.execute('INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)',
                    {'origin':origin, 'destination':destination, 'duration':duration})

        print(f'Added flight from {origin} to {destination}, with duration {duration} minutes.')

    # We commit the db transaction
    db.commit()

if __name__ == '__main__':
    main()
