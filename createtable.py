
import psycopg2
import connection

conn = connection.get_connection()
cur = conn.cursor()
cur.execute("""

DROP TABLE IF EXISTS News;

CREATE TABLE News
(ID INT PRIMARY KEY NOT NULL,
CONTENT TEXT NOT NULL
);

DROP TABLE IF EXISTS Entity;

CREATE TABLE Entity
(ID INT NOT NULL,
ENTITY_CATEGORY TEXT NOT NULL,
ENTITY_NAME TEXT NOT NULL,
COUNT INT NOT NULL

);
""")

conn.commit()
print("table created successfully")
conn.close()