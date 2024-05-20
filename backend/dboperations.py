import os
from dotenv import load_dotenv

import psycopg2

load_dotenv('./.env')

# kaustav comment
# dbname = 'acloudguruji'
# user = 'postgres'
# password = 'Mousumi@25'
# host = 'localhost'
# port = '5432'

dbname = os.environ["dbname"]
user = os.environ["user"]
password = os.environ["password"]
host = os.environ["host"]
port = os.environ["port"]

def get_item_details(barcode):
    item = None
    conn_str = f"dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'"
    try:
        with psycopg2.connect(conn_str) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT product_id, product_name, product_price, product_stock FROM products WHERE barcode = %s", (barcode,))
                item = cursor.fetchone()
    except Exception as e:
        print("Database connection failed due to {}".format(e))
    
    return item
