from flask import *
import sqlite3
app = Flask(__name__)
connection = sqlite3.connect("database.sqlite")
cursor = sqlite3.Cursor(connection)

def make_product_card(info):
    products = cursor.execute("SELECT * FROM products").fetchall()
    for product in products:
        cards.append(make_product_card(product))
    name = str(info[1])
    description = str(info[2])
    price =str(info[3]) + "UAH"

    return f'<div class="services"> <div class="service-box"><h4>{name}</h4><p>{description}</p></div>'



@app.route('/')
def index():
    return render_template('main.html')

@app.route("/result")
def result():

    cards = make_product_card()

    return render_template('product.html', products=cards)

app.run(debug=True)
