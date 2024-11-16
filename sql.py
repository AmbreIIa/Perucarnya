import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = sqlite3.Cursor(connection)


request = ("CREATE TABLE IF NOT EXISTS products"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "price INTEGER)")


cursor.execute(request)

insert_request = ("INSERT INTO products"
                  "(name,price) VALUES(?,?)")

cursor.execute(insert_request, ("стрижка" , "270 грн"))
cursor.execute(insert_request, ("фарбування " , "250 грн"))
cursor.execute(insert_request, ("укладання" , "150 грн"))

text = cursor.execute("SELECT * FROM products")
print(text.fetchall())
