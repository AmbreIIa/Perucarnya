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

@app.route('/strizhkamasters')
def strizhkamasters():
    conn = get_db_connection()
    cursor = conn.cursor()
    response = cursor.execute("SELECT * FROM strizhka")
    masters = response.fetchall()
    return render_template("masters.html", masters=masters)


@app.route('/farbmasters')
def farbmasters():
    conn = get_db_connection()
    cursor = conn.cursor()
    response = cursor.execute("SELECT * FROM farb")
    masters = response.fetchall()
    return render_template("masters.html", masters=masters)


@app.route('/ukladmasters')
def ukladmasters():
    conn = get_db_connection()
    cursor = conn.cursor()
    response = cursor.execute("SELECT * FROM ukladka")
    masters = response.fetchall()
    return render_template("masters.html", masters=masters)


if __name__ == "__main__":
    app.run(debug=True)
