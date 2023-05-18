from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import json
import os


file_path = os.path.join(os.path.dirname(__file__), 'config.json')

with open(file_path,'r') as c:
    params = json.load(c)["params"]
local_server = True

app = Flask(__name__)
app.config['MYSQL_HOST'] = params['mysql_host']  # MySQL host address
app.config['MYSQL_USER'] = params['mysql_user']  # MySQL username
app.config['MYSQL_PASSWORD'] = params['mysql_pass']  # MySQL password
app.config['MYSQL_DB'] = params['mysql_db']  # MySQL database name
mysql = MySQL(app)


# -----------------------------------------------------------------------------------------------

@app.route("/")
def Index():
    string = "Hello World!"
    return render_template("index.html", data = string )

# -----------------------------------------------------------------------------------------------
@app.route("/users")
def Users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users;")
    results = cur.fetchall()
    cur.close()
    return render_template("users.html", rows = results)


# -----------------------------------------------------------------------------------------------

@app.route("/new_user")
def New_user():
    
    return render_template("new_user.html" )

# -----------------------------------------------------------------------------------------------

@app.route("/add_user" , methods=['GET', 'POST'] )
def add_user():
    msg = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        role = request.form.get('role')
        
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s);", (name, email, role))
            mysql.connection.commit()
            cur.close()
            msg = 'User Created Successfully'
        except:
            msg = 'Somthing Went Wronge! User Creation Failed'

    return render_template("new_user.html", msg = msg )


# -----------------------------------------------------------------------------------------------

@app.route("/single_user")
def single_user():
    
    return render_template("single_user.html" )


# -----------------------------------------------------------------------------------------------
@app.route("/user_id", methods=['GET','POST'])
def User_id():
    User_data = None
    if request.method == 'POST':
        id = request.form.get('userid')
        try:
            cur = mysql.connection.cursor()
            print(User_data)
            cur.execute("SELECT * FROM users WHERE id = %s", (id))
            User_data = cur.fetchone()
            cur.close()
            print(User_data)
            if User_data != None:
                msg = 'User Details of Id : '+ id
            else:
                msg = "User Not Found!"
        except:
            msg = 'Somthing Went Wronge! Please Retry'

    return render_template("single_user.html", user_data= User_data , msg = msg)


# -----------------------------------------------------------------------------------------------
@app.route("/user_id/<int:id>")
def User_one(id):
    User_data = None
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (id,))
    User_data = cur.fetchone()
    cur.close()
    if User_data != None:
        msg = 'User Details of Id : '+ str(id)
    else:
        msg = "User Not Found!"

    return render_template("user_one.html", user_data= User_data , msg = msg)

# -----------------------------------------------------------------------------------------------



if __name__ == "__main__":
    app.run(debug=True)