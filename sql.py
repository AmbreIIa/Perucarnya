import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS strizhka")
cursor.execute("DROP TABLE IF EXISTS farb")
cursor.execute("DROP TABLE IF EXISTS ukladka")

request = ("CREATE TABLE IF NOT EXISTS products"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255),"
           "price INTEGER)")

cursor.execute(request)

insert_request = ("INSERT INTO products"
                  "(name, description, price) VALUES(?, ?, ?)")

cursor.execute(insert_request, ("стрижка", "Класичні та сучасні стрижки для будь-якого віку та стилю.", 270))
cursor.execute(insert_request, ("фарбування", "Професійне фарбування з використанням якісної косметики.", 250))
cursor.execute(insert_request, ("укладання", "Ідеальні укладки для будь-якої події – від повсякденних до весільних.", 250))

request = ("CREATE TABLE IF NOT EXISTS strizhka"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "age INTEGER,"
           "description VARCHAR(255))")

cursor.execute(request)

insert_request = ("INSERT INTO strizhka"
                  "(name, age, description) VALUES(?, ?, ?)")

cursor.execute(insert_request, ("Ольга", 23, " 2 роки"))
cursor.execute(insert_request, ("Іван", 30, " 5 років"))
cursor.execute(insert_request, ("Анна ", 25, " 4 роки"))
cursor.execute(insert_request, ("Дмитро", 18, " 1 рік"))

request = ("CREATE TABLE IF NOT EXISTS ukladka"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "age INTEGER,"
           "description VARCHAR(255))")

cursor.execute(request)

insert_request = ("INSERT INTO ukladka"
                  "(name, age, description) VALUES(?, ?, ?)")

cursor.execute(insert_request, ("Олександр", 28, " 6 років"))
cursor.execute(insert_request, ("Олександра ", 22, " 1 рік"))
cursor.execute(insert_request, ("Василь ", 25, " 4 роки"))

request = ("CREATE TABLE IF NOT EXISTS farb"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "age INTEGER,"
           "description VARCHAR(255))")

cursor.execute(request)

insert_request = ("INSERT INTO farb"
                  "(name, age, description) VALUES(?, ?, ?)")

cursor.execute(insert_request, ("Марк ", 28, "7 років"))
cursor.execute(insert_request, ("Владислав", 40, " 12 років"))
cursor.execute(insert_request, ("Артур ", 33, " 9 років"))

text = cursor.execute("SELECT * FROM products")
print(text.fetchall())

connection.commit()
connection.close()
