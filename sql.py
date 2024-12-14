import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()

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
cursor.execute(insert_request, ("укладання", "Ідеальні укладки для будь-якої події – від повсякденних до весільних.", 150))

request = ("CREATE TABLE IF NOT EXISTS strizhka"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255))")

cursor.execute(request)

insert_request = ("INSERT INTO strizhka"
                  "(name, description) VALUES(?, ?)")

cursor.execute(insert_request, ("Ольга 23 роки", "Стаж роботи 2 роки"))
cursor.execute(insert_request, ("Іван 30 років", "Стаж роботи 5 років"))
cursor.execute(insert_request, ("Анна 25 років", "Стаж роботи 4 роки"))

request = ("CREATE TABLE IF NOT EXISTS ukladka"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255))")

cursor.execute(request)

insert_request = ("INSERT INTO ukladka"
                  "(name, description) VALUES(?, ?)")

cursor.execute(insert_request, ("Олександр 28 років", "Стаж роботи 6 років"))
cursor.execute(insert_request, ("Олександра 22 роки", "Стаж роботи 1 рік"))
cursor.execute(insert_request, ("Василь 25 років", "Стаж роботи 4 роки"))

request = ("CREATE TABLE IF NOT EXISTS farb"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255))")

cursor.execute(request)

insert_request = ("INSERT INTO farb"
                  "(name, description) VALUES(?, ?)")

cursor.execute(insert_request, ("Марія 23 роки", "Стаж роботи 2 роки"))
cursor.execute(insert_request, ("Володимир 30 років", "Стаж роботи 5 років"))
cursor.execute(insert_request, ("Анна 25 років", "Стаж роботи 4 роки"))

text = cursor.execute("SELECT * FROM products")
print(text.fetchall())

connection.commit()
connection.close()
