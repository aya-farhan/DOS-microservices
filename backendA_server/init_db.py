import sqlite3

connection = sqlite3.connect('database.db')


with open("schema.sql") as f:
    connection.executescript(f.read())


cur = connection.cursor()


                          
sqlite_insert_query_0 = """INSERT INTO books
                          (id, name, topic, cost, number_of_items) 
                           VALUES 
                          (1,'How to get a good grade in DOS in 40 minutes a day','distributed systems',30,10)"""
                          
sqlite_insert_query_1 = """INSERT INTO books
                          (id, name, topic, cost, number_of_items) 
                           VALUES 
                          (2,'RPCs for Noobs','distributed systems',50,4)"""

sqlite_insert_query_2 = """INSERT INTO books
                          (id, name, topic, cost, number_of_items) 
                           VALUES 
                          (3,'Xen and the Art of Surviving Undergraduate School','undergraduate school',50,4)"""
                          
sqlite_insert_query_3 = """INSERT INTO books
                          (id, name, topic, cost, number_of_items) 
                           VALUES 
                          (4,'Cooking for the Impatient Undergrad','undergraduate school',50,4)"""
                          
                                                    
cur.execute(sqlite_insert_query_0)
cur.execute(sqlite_insert_query_1)
cur.execute(sqlite_insert_query_2)
cur.execute(sqlite_insert_query_3)

connection.commit()
connection.close()

