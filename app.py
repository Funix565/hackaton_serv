#!flask/bin/python
from flask import Flask
import psycopg2
import json

con = psycopg2.connect(
  database="hack", 
  user="sergres", 
  #user="postgres",
  password="password", 
  #password="Kumkva2021",
  host="204.2.63.23", 
  #host="127.0.0.1",
  port="24192"
  #port="5432"
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
    return json.dumps(result)

    # get news title, desc, img, date
    # get full news


@app.route('/news/list/')
def show() :
    cur = con.cursor()
    cur.execute("SELECT news_date, contents, news_pic_url FROM news LIMIT 10")
    rows = cur.fetchall()
    if (rows == []) :
        result = {
            "status" : "null"
        }
        return json.dumps(result)
    else :
        string_res = ""
        for rec in rows :
            result = {
                "status": "not null",
                "news_date": str(rec[0]),
                "contents": rec[1],
                "news_pic_url": rec[2]
            }
            string_res += json.dumps(result)
        string_res += "]"
        return string_res

# write get for concrete article

@app.route('/news/<int:id_news>/')
def publish(id_news) :
    cur = con.cursor()
    cur.execute("SELECT id_news, news_date, contents, news_text, author, news_pic_url FROM news WHERE id_news = %s", (id_news,))
    rows = cur.fetchone()
    if (rows == None) :
        result = {
            "status" : "Fail"
        }
        return json.dumps(result)
    else :
        result = {
            "status" : "Success",
            "news_date" : str(rows[1]),
            "contents" : rows[2],
            "news_text" : rows[3],
            "author" : rows[4],
            "news_pic_url" : rows[5]
        }
        return json.dumps(result)

@app.route('/goods/list/')
def see_goods() :
    cur = con.cursor()
    cur.execute("SELECT name, price, link FROM goods LIMIT 10")
    rows = cur.fetchall()
    if (rows == []) :
        result = {
            "status" : "null"
        }
        return json.dumps(results)
    else :
        string_res = ""
        for rec in rows :
            result = {
                "status" : "not null",
                "name" : rec[0],
                "price" : rec[1],
                "link" : rec[2]
            }
            string_res += json.dumps(result)
        string_res += "]"
        return string_res

@app.route('/goods/<int:goods>/')
def buy_g(goods) :
    cur = con.cursor()
    cur.execute("SELECT goods, name, description, price, link FROM goods WHERE goods = %s", (goods,))
    rows = cur.fetchone()
    if (rows == None) :
        result = {
            "status" : "Fail"
        }
        return json.dumps(result)
    else :
        result = {
            "status" : "not null",
            "name" : rows[1],
            "description" : rows[2],
            "price" : rows[3],
            "link" : rows[4]
        }
        return json.dumps(result)

@app.route('/excursions/list/')
def see_excurs() :
    cur = con.cursor()
    cur.execute("SELECT name, price, link FROM excursions LIMIT 10")
    rows = cur.fetchall()
    if (rows == []) :
        result = {
            "status" : "null"
        }
        return json.dumps(results)
    else :
        string_res = ""
        for rec in rows :
            result = {
                "status" : "not null",
                "name" : rec[0],
                "price" : rec[1],
                "link" : rec[2]
            }
            string_res += json.dumps(result)
        string_res += "]"
        return string_res

@app.route('/excursions/<int:excursions>/')
def buy_excurs(excursions) :
    cur = con.cursor()
    cur.execute("SELECT excursions, triales, price, description, link, name FROM excursions WHERE excursions = %s", (excursions,))
    rows = cur.fetchone()
    if (rows == None) :
        result = {
            "status" : "Fail"
        }
        return json.dumps(result)
    else :
        result = {
            "status" : "not null",
            "triales" : rows[1],
            "price" : rows[2],
            "description" : rows[3],
            "link" : rows[4],
            "name" : rows[5]
        }
        return json.dumps(result)







if __name__ == '__main__':
    app.run(debug=True)