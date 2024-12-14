from flask import *
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("database.sqlite")
    connection.row_factory = sqlite3.Row
    return connection


def make_product_card(product):
    name = str(product['name'])
    description = str(product['description'])
    price = str(product['price']) + " UAH"

    return f'<div class="services"> <div class="service-box"><h4>{name}</h4><p>{description}</p><p>{price}</p></div></div>'


@app.route('/')
def index():
    return render_template('main.html')


@app.route("/result")
def result():
    connection = get_db_connection()
    cursor = connection.cursor()

    products = cursor.execute("SELECT * FROM products").fetchall()
    connection.close()
1
    cards = ""
    for product in products:
        cards += make_product_card(product)

    return render_template('product.html', products=cards)


if __name__ == "__main__":
    app.run(debug=True)
