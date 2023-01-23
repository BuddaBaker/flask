import sqlite3

class Student:
    def __init__(self):
        self.name = ""
        self.classOf = ""
        self.dob = ""
        self.age = 0
        self.favorite_cuisine = ""
        self.favorite_restaurant = ""
        try:
            self.conn = sqlite3.connect('/home/prasithchilla/vscode/flask/volumes/students.db')
            self.create_table()
        except sqlite3.Error as e:
            print(f'Error: {e}')
            print('Could not connect to the database, please make sure the file path is correct and the user has the necessary permissions')

    def create_table(self):
        c = self.conn.cursor()
        try:
            c.execute('''CREATE TABLE IF NOT EXISTS students
                         (name text, classOf text, dob text, age int, favorite_cuisine text, favorite_restaurant text)''')
            self.conn.commit()
            print("Table created successfully")
        except sqlite3.Error as e:
            print(f'Error creating table: {e}')
        c.close()

    def get_user_input(self):
        self.name = input("What is your name? ")
        self.classOf = input("What is your class of? ")
