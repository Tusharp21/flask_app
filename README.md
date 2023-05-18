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

#### representation of the schema
1. Users Database:

2. Users Table:
```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  role VARCHAR(255)
);
```
**id** is an integer column and serves as the primary key.
**name** is a varchar column that stores the user's name.
**email** is a varchar column that stores the user's email address.
**role** is a varchar column that stores the user's role or job title.

3. Users Table Data:
```sql
INSERT INTO users (id, name, email, role)
VALUES
  (1, 'Tushar', 'ptushar139@gmail.com', 'Devloper'),
  (2,'Tushar', 'ptusharwrk139@gmail.com', 'Devloper2'),
  (3,'Tushar', 'ptusharsec139@gmail.com', 'Devloper3');
```
- we use the INSERT INTO statement to specify the table name (users) and the columns (id, name, email, and role) into which we want to insert data. The VALUES keyword is used to provide the actual values for each row to be inserted.

- Each row of values is enclosed within parentheses and separated by commas. In this case, we inserted three sample rows into the "users" table, representing different users with their respective information.

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

#### Git Workflow
1. **Fork the Repository**: Start by forking the repository on GitHub. This creates a copy of the project under my GitHub account.

2. **Clone the Repository**: Clone the forked repository to my local machine using the git clone command. This will create a local copy of the project.

3. **Create a Branch**: Create a new branch on my local repository (steptech_assignment) using the git branch command. Branches allow you to isolate your changes from the main codebase.

4. ** Switch to the Branch**: Switch to the newly created branch using the git checkout command.

5. ** Make Changes**: Make the necessary changes to the project files using VS Code

6. **Commit Changes**: Use the git add command to stage the changes, and then commit them using the git commit command. Provide a descriptive commit message that explains the changes.

7. **Push Changes**: Push local branch with the changes to forked repository on GitHub using the git push command.

8. **Create a Pull Request**: Go to the original repository on GitHub and create a new Pull Request (PR) from pushed branch. This notifies the about proposed changes.

9. **Make Changes and Update**: If any changes are requested, make the necessary modifications in my local branch, commit the changes, and push them to forked repository. The PR will be automatically updated with the new changes.

10. **Merge Pull Request**: Now merge pull request into the main codebase.


#### Outputs :

- 1 home: 

- 2 users: 

- 3 new_user: 

- 4 single_user: 

- 5 one_user: 

