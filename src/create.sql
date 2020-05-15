CREATE TABLE passengers (
  id  SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  flight_id INT NOT NULL REFERENCES flights
);
