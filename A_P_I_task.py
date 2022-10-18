import json
from operator import methodcaller
from flask import Flask , request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host = "localhost", user = 'root', passwd = "KuShi025" )
cursor =  mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable(name varchar(20), mobile_No int(10))")
# cursor.execute("show databases")
# print(cursor.fetchall())


@app.route("/info", methods = ['POST'])
def info():
    if request.method == "POST":    
        name  = request.json["name"]
        mobile  = request.json["mobile_No"]
        cursor.execute("insert into taskdb.tasktable values (%s,%s),(name,  mobile)")
        mydb.commit()
        return jsonify(str("Succesfully inserted"))

if __name__ == '__main__':
    app.run()