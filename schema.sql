CREATE DATABASE student_db;

\c student_db

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    course VARCHAR(100),
    grade VARCHAR(2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);