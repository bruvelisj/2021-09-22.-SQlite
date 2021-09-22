import sqlite3

connect = sqlite3.connect("janistest.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY , 
    user_name TEXT,
    user_tel INTEGER,
    location TEXT
)
""")

connect.commit()

user_list = [6, "Janis", 2345678, "Latvia"]
cursor.execute("INSERT INTO user VALUES(?,?,?,?);", user_list)


connect.commit()

###Ar funkciju 
#def search_db():
   # cursor.execute("SELECT * FROM users")
    #all_results = cursor.fetchall()
   # print(all_results[0][1]) ####  Iesp;ejams otrādi izvilkt datus no datu bāzes


