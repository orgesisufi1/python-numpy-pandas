import mysql.connector 
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')


con = mysql.connector.connect(
    host=host,
    user=user,
    passwd=password,
    database=database
)

cur = con.cursor()

# cur.execute("""
#     CREATE TABLE Contacts (
#     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
#     name VARCHAR(255), 
#     phone_number VARCHAR(255),
#     email VARCHAR(255), 
#     optional_address VARCHAR(255)
#     );
#     """
# )

