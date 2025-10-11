
from venv import create
import psycopg2


class UniversityDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="maktab134",
            user="Hbalforoosh",
            password="1234",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()

    def create_tables(self):
        create_tables = """
        CREATE TABLE IF NOT EXISTS Department (
            department_id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Professor (
            professor_id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            department_id INT REFERENCES Department(department_id)
        );

        CREATE TABLE IF NOT EXISTS Student (
            student_id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            birth_date DATE
        );

        CREATE TABLE IF NOT EXISTS Course (
            course_id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            credits INT NOT NULL,
            professor_id INT NOT NULL REFERENCES Professor(professor_id),
            department_id INT NOT NULL REFERENCES Department(department_id)
        );

        CREATE TABLE IF NOT EXISTS Enrollment (
            enrollment_id SERIAL PRIMARY KEY,
            student_id INT NOT NULL REFERENCES Student(student_id),
            course_id INT NOT NULL REFERENCES Course(course_id),
            enrollment_date DATE NOT NULL
        );
        """
        self.cur.execute(create_tables)
        self.conn.commit()

    def insert_sample_data(self):

        departments = [
            ('Python'),
            ('C++'),
            ('Ai'),
            ('Java')
        ]
        self.cur.executemany(
            "INSERT INTO Department (name) VALUES (%s)", departments)

        professors = [
            ('Dr. Maleki', 1),
            ('Dr. Ghotbi', 2),
            ('Dr. Yadegari', 3),
            ('Dr. Gholami', 4)
        ]
        self.cur.executemany(
            "INSERT INTO Professor (name, department_id) VALUES (%s, %s)", professors)

        students = [
            ('Ramin', '2005-05-15', 'Ramin@example.com'),
            ('Nilofar', '2008-08-22', 'Nilofar@example.com'),
            ('Zahra', '2006-03-10', 'Zahra@example.com'),
            ('Atefeh', '2004-11-05', 'AtefeH@example.com'),
        ]
        self.cur.executemany(
            "INSERT INTO Student (name, birth_date, email) VALUES (%s, %s, %s)", students)

        courses = [
            ("Argparse", 2, 1, 1),
            ("AI", 4, 2, 3),
            ("java", 1, 3, 4),
            ("C", 3, 4, 2),
        ]
        self.cur.executemany(
            "INSERT INTO courses (title, credits, professor_id, department_id) VALUES (%s, %s, %s, %s)", courses)
        enrollments = [
            (1, 1, '2025-9-05'), (1, 4, '2025-09-01')
        ]
        self.cur.executemany(
            "INSERT INTO Enrollment (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)", enrollments)

    def queries(self):
