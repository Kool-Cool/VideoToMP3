import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv


server = Flask(__name__)
mysql = MySQL(server)


#config
load_dotenv()
server.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
# export MYSQL_HOST = localhost
print(server.config["MYSQL_HOST"])
