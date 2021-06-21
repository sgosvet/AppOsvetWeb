# Creating a Table
import pymysql
# database connection
db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="root",
                     database="pythondatabase")

# Make sure to initiate the cursor to fetch rows
cursor = db.cursor()
# Create a Table
students_info = """CREATE TABLE students_info(
                   ID INT(20) PRIMARY KEY AUTO_INCREMENT,
                   NAME  CHAR(20) NOT NULL,
                   AGE INT(3))"""
cursor.execute(students_info)
print(db)
# make a habit to close the database connection once you create it
db.close()



# Insert Queries
# database connection
db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="root", database="pythondatabase")


# Make sure to initiate the cursor to fetch rows
cursor = db.cursor()

# Create a Table
students_info = """CREATE TABLE students_info(
                    ID INT(20) PRIMARY KEY AUTO_INCREMENT,
                    NAME  CHAR(20) NOT NULL,
                    AGE INT(3))"""

# insert queries
row1 = "INSERT INTO students_info(NAME, AGE) VALUES('Smith', 21);"
row2 = "INSERT INTO students_info(NAME, AGE) VALUES('John', 19);"
# executing the quires
cursor.execute(row1)
cursor.execute(row2)
print(db)
# commit the connection
db.commit()
# make a habit to close the database connection once you create it
db.close()


# Select in Python MySQL
# database connection
db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="root",
                     database="pythondatabase")

# Make sure to initiate the cursor to fetch rows
cursor = db.cursor()

# fetch all the queries in students_info Table
fetch_queries = "Select * from students_info;"

# queries execution
cursor.execute(fetch_queries)
lines = cursor.fetchall()
for line in lines:
    print(line)

# commit the connection
db.commit()

# make a habit to close the database connection once you create it
db.close()

# Output will be like:
# (1, 'Smith', 21)
# (2, 'John', 19)

# Update in Python MySQL
# Update an Attribute Value in the Table
update_name = "UPDATE students_info SET NAME= 'Lana'  WHERE ID = '1' ;"
cursor.execute(update_name)

# Delete in Python MySQL
# Delete a query
delete_query = "DELETE FROM students_info WHERE ID = '1'; "
cursor.execute(delete_query)

# Drop Table in Python MySQL
# Drop an entire table
drop_table = "DROP TABLE IF EXISTS students_info;"
cursor.execute(drop_table)
