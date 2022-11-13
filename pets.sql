DROP DATABASE IF EXISTS pet_database;

CREATE DATABASE pet_database;

\c pet_database

CREATE TABLE pets
    (id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INTEGER,
    notes TEXT,
    available BOOLEAN NOT NULL);
