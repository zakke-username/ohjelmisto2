from flask import Flask, request
import mysql.connector

app = Flask(__name__) 

db_connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="",
    password="",
    autocommit=True
)

@app.route("/kenttä/<icao>")
def get_airport_info(icao):
    sql = f"select ident, name, municipality from airport where ident = '{icao}'"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    response = {
        "ICAO": result[0][0],
        "Name": result[0][1],
        "Municipality": result[0][2]
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)