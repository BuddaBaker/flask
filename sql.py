import sqlite3

class Student:
    def __init__(self):
        self.name = ""
        self.classOf = ""
        self.dob = ""
        self.age = 0
        self.favorite_cuisine = ""
        self.favorite_restaurant = ""
        self.conn = sqlite3.connect('/home/prasithchilla/vscode/flask/volumes/students.db') # Connects to or creates the '/home/prasithchilla/vscode/flask/volumes/students.db' file
        self.create_table() # Creates the students table

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS students
                     (name text, classOf text, dob text, age int, favorite_cuisine text, favorite_restaurant text)''')
        self.conn.commit()
        c.close()

    def get_user_input(self):
        self.name = input("What is your name? ")
        self.classOf = input("What is your class of? ")
        dob_input = input("What is your date of birth (yyyy-mm-dd)? ")
        self.dob = datetime.strptime(dob_input, "%Y-%m-%d")
        self.age = self.calculate_age()
        self.favorite_cuisine = input("What is your favorite cuisine? ")
        self.favorite_restaurant = input("What is your favorite restaurant? ")

    # rest of the code
