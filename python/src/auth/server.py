import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv


server = Flask(__name__)
mysql = MySQL(server)


#config
load_dotenv()
server.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
server.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
server.config["MYSQL_PORT"] = os.getenv("MYSQL_PORT")



@server.route("/login" , method = ["POST"])
def login():
    auth  = request.authorization
    # authentication header
    if not auth :
        return "missing credemtialsss !!",401
    # else:
    #     # check db for username and password
    #     return "Cheking in db!!
  
    


