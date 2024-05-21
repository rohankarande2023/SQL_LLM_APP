import sqlite3

# Connect to sqlite

connection=sqlite3.connect("student.db")

## Create cursor object to insert, create table retrieve etc

cursor=connection.cursor()


## Create a table

table_info="""
CREATE TABLE StudentRecords (
    Student VARCHAR(100),
    Class VARCHAR(50),
    Section VARCHAR(30),
    Marks INT
);

"""

cursor.execute(table_info)


## Insert records in StudentRecords table

cursor.execute("""INSERT INTO StudentRecords (Student, Class, Section, Marks) VALUES
('Alice Johnson', '10th Grade', 'A', 85),
('Bob Smith', '10th Grade', 'B', 90),
('Charlie Brown', '11th Grade', 'A', 88),
('Daisy Miller', '11th Grade', 'C', 92);
""")


## Display records

data=cursor.execute("""Select * from StudentRecords""")

for row in data:
    print(row)

# Close connection

connection.commit()
connection.close()
