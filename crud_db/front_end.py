from setup import create_connection, create_table
from controller import create_row, createRow, get_all_data, delete_record

conn = create_connection("qa-db")
cursor = conn.cursor()

# create_table_string = "CREATE TABLE people (people_id int NOT NULL UNIQUE, height varchar NOT NULL, people_name varchar(30) NOT NULL, PRIMARY KEY (people_id));"
# create_table(cursor, create_table_string)

# createRow(conn, "INSERT INTO people VALUES(1, 5.11, 'Jonas'), (2, 6.00, 'Hadoin');")
# print(get_all_data(conn, "people"))

def user_input():
    print(
        """
        Welcome to the DB!
        Please select an option, entering the number
        1. Create Data
        2. Get All Data
        3. Delete Data
        """
        )
    choice = input("Please enter an option: ")

    if choice == "1":
        create_row_console()
    elif choice == "2":
        get_all_data()
    elif choice == "3":
        delete_record_console()
    elif choice == "4":
        print(single_record)

def create_row_console():
    id = input("Please enter people id: ")
    height = input("Please enter height: ")
    name = input("Please enter name of person: ")
    query = f"INSERT INTO people VALUES({id}, '{height}', {name});"

    create_row(conn, query)

def delete_record_console():
    name = input("Please enter name to delete: ")
    user_input=input(str"Are you sure you want to delete? : YES/NO")
    if user_input == "YES":
        print(delete_record(conn, name))

user_input()