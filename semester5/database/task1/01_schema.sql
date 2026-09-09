DROP TABLE IF EXISTS load CASCADE;
DROP TABLE IF EXISTS subject CASCADE;
DROP TABLE IF EXISTS teacher CASCADE;
DROP TABLE IF EXISTS ranks CASCADE;
DROP TABLE IF EXISTS departments CASCADE;
DROP TYPE IF EXISTS payment_enum;

CREATE TYPE payment_enum AS ENUM ('оклад', 'почасовая');

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name TEXT NOT NULL
);

CREATE TABLE ranks (
    rank_id INT PRIMARY KEY,
    rank_name TEXT NOT NULL
);

CREATE TABLE teacher (
    teacher_id INT PRIMARY KEY,
    first_name TEXT NOT NULL,
    surname_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    department_id INT REFERENCES departments(department_id),
    rank_id INT REFERENCES ranks(rank_id),
    payment_type payment_enum NOT NULL,
    base_rate INT NOT NULL,
    allowance INT DEFAULT 0,
    number_of_children INT DEFAULT 0
);

CREATE TABLE subject (
    subject_id INT PRIMARY KEY,
    subject_name TEXT NOT NULL,
    department_id INT REFERENCES departments(department_id)
);

CREATE TABLE load (
    teacher_id INT REFERENCES teacher(teacher_id),
    subject_id INT REFERENCES subject(subject_id),
    number_of_hours INT NOT NULL,
    PRIMARY KEY (teacher_id, subject_id)
);
