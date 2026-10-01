CREATE TABLE IF NOT EXISTS cr2a7_author (
    cr2a7_author_id SERIAL PRIMARY KEY,
    modification_date timestamp,      
    name varchar(100),      
    createdby varchar(100),      
    creation_date timestamp,      
    memberType varchar(100)
);

CREATE TABLE IF NOT EXISTS cr2a7_library (
    cr2a7_library_id SERIAL PRIMARY KEY,
    address varchar(100),      
    Autor_delegado varchar(100),      
    Estado varchar(100)
);

CREATE TABLE IF NOT EXISTS cr2a7_book (
    cr2a7_book_id SERIAL PRIMARY KEY,
    creation_date timestamp,      
    release varchar(100),      
    title varchar(100),      
    modification_date timestamp,      
    pages int,      
    createdby varchar(100)
);

ALTER TABLE cr2a7_author
ADD COLUMN cr2a7_book_id INT REFERENCES cr2a7_book(cr2a7_book_id);

ALTER TABLE cr2a7_book
ADD COLUMN cr2a7_library_id INT REFERENCES cr2a7_library(cr2a7_library_id);

