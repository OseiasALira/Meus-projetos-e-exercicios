"""
Functions 

"""
import sqlite3

class Funcs():
    """ 
    Funções do aplicativo
    
    """
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
            current_year INTEGER NOT NULL,
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
    def add_student(self):
        ...
    def delete_student(self):
        ...
    def update_student(self):
        ...
    def add_quiz(self):
        ...
    def update_quiz(self):
        ...
    def delete_quiz(self):
        ...

teste =Funcs()

teste.db_table()