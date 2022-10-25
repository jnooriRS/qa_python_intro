import sqlite3

conn = sqlite3.connect("new1-db")
cursor = conn.cursor()

createTableQuery = "CREATE TABLE Laptop(Laptop_Id int(11) NOT NULL, Laptop_Name varchar(250) NOT NULL, Price float NOT NULL)"

laptop_data_dump = """INSERT INTO Laptop (Laptop_Id, Laptop_Name, Price) 
                           VALUES 
                           (1, 'Lenovo ThinkPad P71', 6459),
                           (2, 'Area 51M', 6999),
                           (3, 'MacBook Pro', 2499); """
cursor.execute(laptop_data_dump)
#cursor.execute(createTableQuery)
query = "SELECT name FROM sqlite_master"
query2 = "SELECT * FROM Laptop"
data = cursor.execute(query)
data2 = cursor.execute(query2)
print(data.fetchall())
conn.commit()

#xercise - Using sqlite create a database called "new-db" and create a table of your choice with 3+ fields and 1 primary key
# Using the "SELECT name FROM sqlite_master" print out the name of your table 

# user this as refrence for DBs https://pynative.com/python-mysql-insert-data-into-database-table/#:~:text=Insert%20a%20Single%20Row%20into%20MySQL%20table%20from,the%20cursor%20object%20and%20database%20connection%20object%20