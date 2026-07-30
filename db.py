import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
        return psycopg.connect(
            host=os.environ["PGHOST"],
            port=os.environ["PGPORT"],
            user=os.environ["PGUSER"],
            password=os.environ["PGPASSWORD"],
            dbname=os.environ["PGDATABASE"]
        )
