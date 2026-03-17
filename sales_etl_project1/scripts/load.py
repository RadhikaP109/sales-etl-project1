import mysql.connector

def load_data(df, db_config):

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    for index, row in df.iterrows():
        cursor.execute("""
        INSERT INTO sales
        (order_id, customer, product, quantity, price, total_amount, date)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (row['order_id'], row['customer'], row['product'],
         row['quantity'], row['price'], row['total_amount'], row['date']))

    conn.commit()

    cursor.close()
    conn.close()

    print("Data Loaded Successfully")