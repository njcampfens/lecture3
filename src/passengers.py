from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# We create the conection to the database
DATABASE_URL = 'postgres://nestor:{password}@localhost:5432/lecture3'

engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

def main():

    # List all flights
    flights = db.execute('SELECT id, origin, destination, duration FROM flights')
    for flight in flights:
        print(f'Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes')

    # Prompt user to select a flight
    flight_id = int(input('\nFlight ID: '))
    flight = db.execute('SELECT origin, destination duration FROM flights WHERE id = :id',
                        {'id':flight_id}).fetchone()

    if flight is None:
        print('Error: No such flight.')
        return #quit

    # check passengers
    passengers = db.execute('SELECT name FROM passengers WHERE flight_id = :flight_id',
                            {'flight_id': flight_id}).fetchall()

    print('\nPassengers:')
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print('No passengers.')




if __name__ == '__main__':
    main()
