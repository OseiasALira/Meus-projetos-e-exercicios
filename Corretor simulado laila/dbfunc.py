"""
    Funções do aplivativo

"""
import sqlite3


class DatabaseManager():
    """
    Funções de manipulação do banco de dados

    """

    def __init__(self):

        self.db_connect()
        self.db_table()

    def db_connect(self):
        """Connect database and create a cursor"""

        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def db_disconnect(self):
        """Disconnect database"""
        self.conn.close()

    def db_table(self):
        """Create tables in database if not exists"""
        self.db_connect()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name CHAR(50) NOT NULL,
            class_year INTEGER NOT NULL,
            status INTEGER
        );
        """)
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS exams_answers (
            id INTEGER PRIMARY KEY,
            school CHAR(30) NOT NULL,
            portugues CHAR(20) NOT NULL,
            matematica CHAR(20) NOT NULL,
            current_year INTEGER
        );
        """)
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS students_answers (
            id INTEGER PRIMARY KEY,
            student_id INTEGER NOT NULL,
            exam_id INTEGER NOT NULL,
            answer_port CHAR(20) NOT NULL,
            answer_mate CHAR(20) NOT NULL
        );
        """)
        self.conn.commit()
        self.db_disconnect()

    def add_student(self, name, class_year, status=1):
        """Create new students in database"""
        _name = name
        _class_year = class_year
        _status = status
        self.db_connect()
        self.cursor.execute(""" INSERT INTO students (name, class_year, status)
                            VALUES (?, ?, ?)""", (_name, _class_year, _status)
        )
        self.conn.commit()
        self.db_disconnect()

    def delete_student(self, id_student):
        """Remove students from database"""
        _id_student = id_student
        self.db_connect()
        self.conn.execute(""" DELETE FROM students WHERE id = ? """, _id_student)
        self.conn.commit()
        self.db_disconnect()

    def update_student(self, name, class_year, status, id_student):
        """Update database students"""
        _name = name
        _class_year = class_year
        _status = status
        _id = id_student
        self.db_connect()
        self.cursor.execute(""" UPDATE students SET name = ?, class_year = ?, status = ?
                            WHERE id = ?""", (_name, _class_year, _status, _id)
        )
        self.conn.commit()
        self.db_disconnect()

    def add_exam(self, school, portugues, matematica, current_year):
        """Create new exam"""
        _school = school
        _portugues = portugues
        _matematica = matematica
        _current_year = current_year
        self.db_connect()
        self.conn.execute("""INSERT INTO exams_answers (school, portugues, matematica, current_year)
                          VALUES (?, ?, ?, ?)""", (_school, _portugues, _matematica, _current_year)
        )
        self.conn.commit()
        self.db_disconnect()

    def update_exam(self, school, portugues, matematica, current_year, id_exam):
        """Update exam"""
        _school = school
        _portugues = portugues
        _matematica = matematica
        _current_year = current_year
        _id_exam = id_exam
        self.db_connect()
        self.conn.execute(""" UPDATE exams_answers SET school = ?, portugues = ?,
                          matematica = ?, current_year = ? WHERE id = ?""",
                          (_school, _portugues, _matematica, _current_year, _id_exam)
        )
        self.conn.commit()
        self.db_disconnect()

    def delete_exam(self, id_exam):
        """Remove exam"""
        _id_exam = id_exam
        self.db_connect()
        self.conn.execute(""" DELETE FROM exams_answers WHERE id = ?""", _id_exam)
        self.conn.commit()
        self.db_disconnect()

    def students_answers(self, id_student, id_exam, answer_port, answer_mate):
        """Add stundets answers in database"""

        _id_student = id_student
        _id_exam = id_exam
        _answer_port = answer_port
        _answer_mate = answer_mate

        self.db_connect()
        self.conn.execute(""" INSERT INTO students_answers (student_id, exam_id, answer_port,
                          answer_mate) VALUES (?, ?, ?, ?)""",
                          (_id_student, _id_exam, _answer_port, _answer_mate)

        )
        self.conn.commit()
        self.db_disconnect()

    def stundets_answers_update(self, id_student, id_exam, answer_port, answer_mate, id_students_answers):
        """ update data answers """
        _id_student = id_student
        _id_exam = id_exam
        _answer_port = answer_port
        _answer_mate = answer_mate
        _id_stundets_answers = id_students_answers

        self.db_connect()
        self.conn.execute(""" UPDATE students_answers SET student_id = ?, exam_id = ?
                          answer_port = ?, answer_mate = ? WHERE id = ?""",
                          (_id_student, _id_exam, _answer_port, _answer_mate, _id_stundets_answers)
        )
        self.conn.commit()
        self.db_disconnect()

if __name__ == '__main__':
    DatabaseManager()
    