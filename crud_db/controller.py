# Purpose to create data using the conenction object and query

def create_row(conn, query):
    conn.cursor().execute(query)
    conn.commit()
    return True

def get_all_data(conn, table_name):
    data = conn.cursor().execute(f"SELECT * FROM {table_name}")
    list_data = data.fetchall() # data is useable and readable
    return list_data

def get_single_record(conn, name):
    data = conn.cursor().execute(f"SELECT * FROM people WHERE name == {name}")
    listData = data.fetchall()
    return listData 

def delete_record(conn, table_name, name):
    single_data = conn.cursor().execute(f"DELETE FROM {table_name} WHERE name == {name}")
    return True