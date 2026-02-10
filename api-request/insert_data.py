from api_request import fetch_data, mock_fetch_data, api_url
import psycopg2

def connect_to_database():
    print("Connecting to the PostgreSQL database...")

    try:
        conn = psycopg2.connect(
            host="postgres",
            port=5432,
            dbname="db_psql",
            user="user_psql",
            password="pw_psql"
        )
        return conn
    
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise

def create_table(conn):
    print("Creating table table if it doesn't exist...")

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE SCHEMA IF NOT EXISTS dev;
                CREATE TABLE IF NOT EXISTS dev.financial_data (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMPZ,
                    ask NUMERIC,
                    bid NUMERIC,
                    mid NUMERIC,
                    symbol VARCHAR(10),
                );
            """)
            conn.commit()
            print("Table created successfully.\n")
    
    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        raise

def insert_data(conn, data):
    print("Inserting financial data into the database...")

    try:
        with conn.cursor() as cursor:
            for record in data:  # Insert only the record for the most recent date
                cursor.execute("""
                    INSERT INTO dev.financial_data (timestamp, ask, bid, mid, symbol)
                    VALUES (%s, %s, %s, %s, %s);
                """, (
                    record['timestamp'],
                    record['ask'],
                    record['bid'],
                    record['mid'],
                    record['symbol']
                ))
            conn.commit()
            print("Data inserted successfully.\n")
    
    except psycopg2.Error as e:
        print(f"Failed to insert data: {e}")
        raise

def run():
    try:
        data = mock_fetch_data(api_url)
        conn = connect_to_database()
        create_table(conn)
        insert_data(conn, data)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Database connection closed.")