"""
    Funções do aplivativo

"""
import sqlite3


class Funcs():
    """
    Funções de manipulação do banco de dados
    
    """

    def __init__(self):
        
        self.db_table()

    def db_connect(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def db_disconnect(self):
        self.conn.close()

    def db_table(self):
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
        _name = name
        _class_year = class_year
        _status = status
        self.db_connect()
        self.cursor.execute(""" INSERT INTO students (name, class_year, status)
                            VALUES (?, ?, ?)""", (_name, _class_year, _status))
        self.conn.commit()
        self.db_disconnect()

    def delete_student(self):
        ...

    def update_student(self):
        ...

    def add_exam(self):
        ...

    def update_exam(self):
        ...

    def delete_exam(self):
        ...


Funcs()
