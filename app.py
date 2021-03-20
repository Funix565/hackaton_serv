#!flask/bin/python
from flask import Flask
import psycopg2
import json

con = psycopg2.connect(
  database="hack", 
  user="sergres", 
  password="password", 
  host="204.2.63.23", 
  port="24192"
)

print("Database opened successfully")

app = Flask(__name__)

@app.route('/login/<string:phone>/<string:password>/')
def login(phone, password):
    cur = con.cursor()
    cur.execute("SELECT phone, password FROM customer WHERE phone = %s AND password = %s", ((phone), (password)))
    rows = cur.fetchone()
    if (rows == None) :
        result = {
            "status" : "Fail"
        }
    else :
        result = {
            "status" : "Success"
        }
    con.commit()
    con.close()
    return json.dumps(result)

    # get news title, desc, img, date
    # get full news


@app.route('/news/list/')
def show() :
    cur = con.cursor()
    cur.execute("SELECT news_date, contents, news_text, author, news_pic_url FROM news LIMIT 10")
    rows = cur.fetchall()
    if (rows == []) :
        result = {
            "status" : "null"
        }
        return json.dumps(result)
    else :
        string_res = "[<br>"
        for rec in rows :
            result = {
                "status": "not null",
                "news_date": str(rec[0]),
                "contents": rec[1],
                "news_pic_url": rec[4]
            }
            string_res += json.dumps(result) + "<br>"
        string_res += "]"
        con.commit()
        con.close()
        return string_res

# write get for concrete article


if __name__ == '__main__':
    app.run(debug=True)