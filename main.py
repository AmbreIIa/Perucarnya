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
    masters = conn.execute("SELECT * FROM strizhka").fetchall()
    conn.close()
    return render_template("masters.html", masters=masters)

@app.route('/farbmasters')
def farbmasters():
    conn = get_db_connection()
    masters = conn.execute("SELECT * FROM farb").fetchall()
    conn.close()
    return render_template("masters.html", masters=masters)

@app.route('/ukladmasters')
def ukladmasters():
    conn = get_db_connection()
    masters = conn.execute("SELECT * FROM ukladka").fetchall()
    conn.close()
    return render_template("masters.html", masters=masters)

@app.route('/appointment/<int:master_id>')
def appointment(master_id):
    conn = get_db_connection()
    master = conn.execute(
        "SELECT * FROM strizhka WHERE id = ? UNION "
        "SELECT * FROM farb WHERE id = ? UNION "
        "SELECT * FROM ukladka WHERE id = ?", (master_id, master_id, master_id)
    ).fetchone()
    conn.close()

    if master:
        return render_template("appointment.html", master=master)
    else:
        return "Мастер не найден", 404

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    master_id = request.form.get('master_id')
    date = request.form.get('date')
    time = request.form.get('time')

    conn = get_db_connection()
    conn.execute("INSERT INTO appointments (master_id, date, time) VALUES (?, ?, ?)",
                 (master_id, date, time))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
