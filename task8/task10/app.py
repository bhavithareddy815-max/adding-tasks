from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret_order_key"

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Bhavi__15", # Add your MySQL password here
    "database": "order_tracking_db"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch all orders
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    
    # Fetch daily activity from the View
    cursor.execute("SELECT * FROM daily_order_report")
    report = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('index.html', orders=orders, report=report)

@app.route('/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        customer = request.form['customer_name']
        product = request.form['product_name']
        status = request.form['status']
        amount = request.form['amount']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO orders (customer_name, product_name, status, amount) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (customer, product, status, amount))
        conn.commit()
        cursor.close()
        conn.close()
        
        flash("Order placed successfully!")
        return redirect(url_for('index'))
    
    return render_template('add_order.html')

@app.route('/update_status/<int:order_id>', methods=['POST'])
def update_status(order_id):
    new_status = request.form['new_status']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    # Updating status triggers the log_order_update trigger automatically
    query = "UPDATE orders SET status = %s WHERE order_id = %s"
    cursor.execute(query, (new_status, order_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash(f"Order #{order_id} updated to {new_status}")
    return redirect(url_for('index'))

@app.route('/logs')
def view_logs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # Fetch logs created by the triggers
    cursor.execute("SELECT * FROM order_log ORDER BY changed_at DESC")
    logs = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)