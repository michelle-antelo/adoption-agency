\c pet_database

DROP TABLE IF EXISTS pets;

CREATE TABLE pets
    (id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INTEGER,
    notes TEXT,
    available BOOLEAN NOT NULL);

INSERT INTO pets (name, species, photo_url, age, notes, available)
    VALUES ('Hazel','Cat', 'https://i.pinimg.com/564x/9f/c2/a0/9fc2a0d3ab30d9c20322714eeb66417b.jpg', 2, 'Curious, cuddly, and food motivated!', TRUE);
