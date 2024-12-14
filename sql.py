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

request = ("CREATE TABLE IF NOT EXISTS strizhka"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255)")

cursor.execute(request)

insert_request = ("INSERT INTO strizhka"
                  "(name,price) VALUES(?,?)")

cursor.execute(insert_request, ("Марія 23 рооки" ,"Стаж роботи 2 роки"))
cursor.execute(insert_request, ("Володимир 30 років" ,"Стаж роботи 5 років"))
cursor.execute(insert_request, ("Анна 25 років" ,"Стаж роботи 4 роки"))


request = ("CREATE TABLE IF NOT EXISTS ukladka"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255)")

cursor.execute(request)

insert_request = ("INSERT INTO ukladka"
                  "(name,price) VALUES(?,?)")

cursor.execute(insert_request, ("Олександр 28 рооки" ,"Стаж роботи 6 років"))
cursor.execute(insert_request, ("Олександра 22 рока" ,"Стаж роботи 1 рік"))
cursor.execute(insert_request, ("Василь 25 років" ,"Стаж роботи 4 роки"))


request = ("CREATE TABLE IF NOT EXISTS farb"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255)")

cursor.execute(request)

insert_request = ("INSERT INTO farb"
                  "(name,price) VALUES(?,?)")

cursor.execute(insert_request, ("Марія 23 рооки" ,"Стаж роботи 2 роки"))
cursor.execute(insert_request, ("Володимир 30 років" ,"Стаж роботи 5 років"))
cursor.execute(insert_request, ("Анна 25 років" ,"Стаж роботи 4 роки"))

text = cursor.execute("SELECT * FROM products")
print(text.fetchall())
