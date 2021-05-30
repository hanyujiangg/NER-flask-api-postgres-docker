
import psycopg2

DB_NAME = "mrosbzup"
DB_USER = "mrosbzup"
DB_PASS = "aqNEI7Y05XCIS7GQYdgqc9ksMNxqlhwj"
DB_HOST = "batyr.db.elephantsql.com"
DB_PORT = "5432"

def get_connection():
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                                password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print("database connected successfully")
        return conn
    except:
        print("oops, database not connected")
