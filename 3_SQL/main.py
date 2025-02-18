import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="simple",
    port="8889"
)
cur = my_db.cursor()


sql = 'SELECT id FROM users WHERE login="john"'
cur.execute(sql)
id_user =cur.fetchone()[0]

cur.fetchall()

sql = 'SELECT id FROM items WHERE category="hats"'
cur.execute(sql)
ids_titles =cur.fetchall()

cur.fetchall()

orders_data = [(id_user, item[0]) for item in ids_titles]

sql = 'INSERT INTO orders (user_id, item_id) VALUES (%s, %s)'
cur.executemany(sql, orders_data)
my_db.commit()




sql = 'SELECT user_id, item_id FROM orders'
cur.execute(sql)
orders = cur.fetchall()

print('Все заказы')
for order in orders:
    print(type(order))
    user_id = order[0]
    item_id = order[1]

    sql = 'SELECT login FROM users WHERE id=%s'
    cur.execute(sql, (user_id,))
    user_name = cur.fetchone()[0]

    sql = 'SELECT title FROM items WHERE id=%s'
    cur.execute(sql, (item_id,))
    item_title = cur.fetchone()[0]

    print(f"{user_name}  -  {item_title}")


cur.close()

my_db.close()


