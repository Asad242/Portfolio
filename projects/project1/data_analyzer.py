import sqlite3
import pandas as pd

def create_sample_db():
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                      (id INTEGER PRIMARY KEY, product TEXT, quantity INTEGER, price REAL)''')
    cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Laptop', 10, 999.99)")
    cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Phone', 25, 499.99)")
    cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Tablet', 15, 299.99)")
    conn.commit()
    conn.close()

def analyze_sales():
    conn = sqlite3.connect('sample.db')
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    print("Sales Data:")
    print(df)

    total_revenue = (df['quantity'] * df['price']).sum()
    print(f"\nTotal Revenue: ${total_revenue:.2f}")

    best_seller = df.loc[df['quantity'].idxmax()]['product']
    print(f"Best Selling Product: {best_seller}")
    conn.close()

if __name__ == '__main__':
    create_sample_db()
    analyze_sales()
