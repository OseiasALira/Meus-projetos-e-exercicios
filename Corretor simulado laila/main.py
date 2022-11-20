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
            answers_pt CHAR(20),
            answers_mt CHAR(20)
        );
        """)
        self.conn.commit()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS exams (
            id INTEGER PRIMARY KEY,
            school CHAR(30) NOT NULL,
            answers_pt CHAR(20) NOT NULL,
            answers_mt CHAR(20) NOT NULL,
            year INTEGER
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