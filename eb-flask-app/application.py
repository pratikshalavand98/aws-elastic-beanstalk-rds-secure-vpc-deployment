from flask import Flask
import pymysql

application = Flask(__name__)

DB_HOST = "awseb-e-ytbeqt235q-stack-awsebrdsdatabase-7zqp3ypn023d.cohegwc4804z.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASS = "Pass$123"
DB_NAME = "ebdb"
DB_PORT = 3306

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        port=DB_PORT,
        connect_timeout=5
    )

@application.route("/")
def home():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits(
            id INT AUTO_INCREMENT PRIMARY KEY,
            msg VARCHAR(100)
        )
        """)

        cursor.execute("INSERT INTO visits(msg) VALUES ('Hello from EB')")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM visits")
        count = cursor.fetchone()[0]

        return f"✅ RDS Connected! Visits = {count}"

    except Exception as e:
        return str(e)