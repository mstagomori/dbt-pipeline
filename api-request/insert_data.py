from datetime import datetime
from api_request import fetch_data
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
                CREATE TABLE IF NOT EXISTS dev.weather_data (
                    id SERIAL PRIMARY KEY,
                    city TEXT,
                    temperature FLOAT,
                    weather_descriptions TEXT,
                    wind_speed FLOAT,
                    time TIMESTAMP,
                    inserted_at TIMESTAMP DEFAULT NOW(),
                    utc_offset TEXT
                );
            """)
            conn.commit()
            print("Table created successfully.\n")
    
    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        raise

def insert_data(conn, data):
    print("Inserting weather data into the database...")

    try:
        weather_data = data['current']
        location_data = data['location']
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO dev.weather_data (city, temperature, weather_descriptions, wind_speed, time, inserted_at, utc_offset)
                VALUES (%s, %s, %s, %s, %s, NOW(), %s)
            """, (
                location_data['name'],
                weather_data['temperature'],
                weather_data['weather_descriptions'][0],
                weather_data['wind_speed'],
                location_data['localtime'],
                location_data['utc_offset'],
            ))
            conn.commit()
            print("Data inserted successfully.\n")
    
    except psycopg2.Error as e:
        print(f"Failed to insert data: {e}")
        raise

def run():
    try:
        data = fetch_data()
        conn = connect_to_database()
        create_table(conn)
        insert_data(conn, data)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("Database connection closed.")