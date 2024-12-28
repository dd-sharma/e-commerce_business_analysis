import os
import json
from sqlalchemy import create_engine
import getpass

# Define the path for the credentials file
credentials_file = "db_credentials.json"

def get_credentials():
    """Retrieve credentials from a JSON file or prompt the user to input them."""
    if os.path.exists(credentials_file):
        with open(credentials_file, "r") as file:
            credentials = json.load(file)
            print("Credentials loaded from file.")
    else:
        # Prompt the user for credentials
        credentials = {
            "host": input("Enter MySQL host (e.g., localhost): "),
            "user": input("Enter MySQL username: "),
            "password": getpass.getpass("Enter MySQL password: "),
            "database": input("Enter the MySQL database name: ")
        }
        # Save the credentials to a file
        with open(credentials_file, "w") as file:
            json.dump(credentials, file)
            print("Credentials saved to file.")

    return credentials

def connect_to_database(credentials):
    """Establish a connection to the MySQL database using SQLAlchemy."""
    connection_string = f"mysql+pymysql://{credentials['user']}:{credentials['password']}@{credentials['host']}/{credentials['database']}"
    engine = create_engine(connection_string)
    return engine
