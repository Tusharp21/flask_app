## # Flask Application  Readme

####Requirements
To run the Flask application, make sure you have the following requirements installed on your system:

- Python (version 3.7 or higher)
- pip (Python package installer)
- Flask (Python web framework)
- flask_mysqldb (Python Flask MYSQL library)

####Setup
Follow these steps to set up the Flask application:

1. Clone or download the application source code from the repository.
2. Open a terminal or command prompt and navigate to the project directory.
3. Create a virtual environment (optional but recommended). Run the following command:
 **- Syntex : python3 -m venv flaskenv**
4. Activate the virtual environment. Run the appropriate command:
 **- Syntex : flaskenv\Scripts\activate.bat**
5. Install the required dependencies. Run the following command:
 **- Syntex pip install -r requirements.txt**



#### Configuration
Before running the application, you may need to configure certain settings. Here's how:

1. Open/Create the config.json file in the project directory.
```json
{
    "params" : {
        "mysql_host":"HOSTNAME",
        "mysql_user":"USERNAME",
        "mysql_pass":"PASSWORD",
        "mysql_db":"DATABASE NAME" }
}
```

#### Running the Application
To run the Flask application, follow these steps:

1. Make sure you are in the project directory and the virtual environment is activated (if you created one).
2. In the terminal or command prompt, run the following command:
**- Syntex flask run**
3. The Flask development server should start running. You will see some output indicating that the application is running and listening on a specific address (e.g., http://127.0.0.1:5000/).
4. Open a web browser and navigate to the address shown in the previous '3rd' step.


#### SQL queries used in “Task 2"
a. Create a MySQL database with the name "users" :
**- syntex: CREATE DATABASE users;**

b. Design a table "users" with the following columns :
**- syntex: CREATE TABLE users;**

c. Write SQL queries :
- Insert sample data into the "users" table.
**Syntex: INSERT INTO users (name, email, role) VALUES ("Tushar", "ptusharsec139@gmail.com", "Devloper");**
- Retrieve all users from the "users" table.
**Syntex: SELECT * FROM users;**
- Retrieve a specific user by their ID
**Syntex: SELECT * FROM users WHERE id = 1;**




