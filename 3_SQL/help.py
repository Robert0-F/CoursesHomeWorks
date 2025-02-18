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
#sql = "CREATE DATABASE IF NOT EXISTS `python`"
# sql = "SHOW DATABASES"
# sql = 'CREATE TABLE child (
#     id INT NOT NULL,
#     parent_id INT,
#     PRIMARY KEY(id),
#     FOREIGN KEY(parent_id)
# 		REFERENCES parent(id)
#     	ON DELETE CASCADE
#     ) ENGINE=INNODB'

# sql = 'CREATE TABLE users(name VARCHAR(255), age INT(255))'
# sql = 'SELECT email, SUM(age) AS age, AVG(id) FROM users GROUP BY email;'
# sql = 'INSERT INTO users (email, login, name, date_of_birth, age) VALUES ("help@admin.com", "Admin", "Bob", "2021-01-01", "40");  '

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

cur.close()

my_db.close()


