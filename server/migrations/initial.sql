-- Medium type
CREATE TYPE art_type_enum AS ENUM ("digital", "traditional");

-- Bruh
CREATE TABLE
  IF NOT EXISTS artworks (
    id SERIAL NOT NULL PRIMARY KEY,
    slug VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    date TIMESTAMP NOT NULL,
    description TEXT NOT NULL,
    art_type art_type_enum NOT NULL,
  );

CREATE TABLE
  characters (
    id SERIAL PRIMARY KEY,
    artwork_id INTEGER NOT NULL,
    slug VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    avatar_url VARCHAR NOT NULL,
    full_name VARCHAR,
    species VARCHAR NOT NULL,
    is_hybrid BOOLEAN NOT NULL,
    FOREIGN KEY (artwork_id) REFERENCES artworks (id)
  );

CREATE TABLE
  mediums (
    id SERIAL PRIMARY KEY,
    artwork_id INTEGER NOT NULL,
    medium VARCHAR NOT NULL,
    FOREIGN KEY (artwork_id) REFERENCES artworks (id)
  );