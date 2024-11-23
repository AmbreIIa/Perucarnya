import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = sqlite3.Cursor(connection)


request = ("CREATE TABLE IF NOT EXISTS products"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255)"
           "price INTEGER)")


cursor.execute(request)

insert_request = ("INSERT INTO products"
                  "(name,price) VALUES(?,?,?)")

cursor.execute(insert_request, ("стрижка" , "Класичні та сучасні стрижки для будь-якого віку та стилю.", "270 грн"))
cursor.execute(insert_request, ("фарбування " ,"Професійне фарбування з використанням якісної косметики.", "250 грн"))
cursor.execute(insert_request, ("укладання" ,"Ідеальні укладки для будь-якої події – від повсякденних до весільних.", "150 грн"))

text = cursor.execute("SELECT * FROM products")
print(text.fetchall())
