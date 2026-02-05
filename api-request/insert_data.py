from api_request import fetch_data, mock_fetch_data
import psycopg2

def connect_to_database():
    print("Connecting to the PostgreSQL database...")

    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="postgres",
            user="postgres",
            password="postgres"
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
                    date DATE,
                    open NUMERIC,
                    high NUMERIC,
                    low NUMERIC,
                    close NUMERIC,
                    volume NUMERIC
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
            for record in data[0]:  # Insert only the record for the most recent date
                cursor.execute("""
                    INSERT INTO dev.financial_data (date, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (
                    record['date'],
                    record['open'],
                    record['high'],
                    record['low'],
                    record['close'],
                    record['volume']
                ))
            conn.commit()
            print("Data inserted successfully.\n")
    
    except psycopg2.Error as e:
        print(f"Failed to insert data: {e}")
        raise

def main():
    try:
        data = mock_fetch_data()  # Use mock data for testing
        conn = connect_to_database()
        create_table(conn)
        insert_data(conn, data)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Database connection closed.")

main()
