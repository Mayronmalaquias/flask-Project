from flask import Flask, render_template, request, session, make_response
import pymysql
app = Flask(__name__)


app.secret_key = "QIUWEYQUIWEYQIU"


db = pymysql.connect(host = "localhost", user="root", password="blablabla", database="youtube")


@app.route("/", methods=['GET', 'POST'])
def hello_word():
    if request.method == "GET":
        resp = make_response("Meu website")
        if request.cookies.get('usuario'):
            resp = make_response("Meu website com cookie setado.")
        else:
            resp = make_response("Meu website sem cookie!")
            resp.set_cookie("usuario", "guilherme")

        cursor = db.cursor()
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        return resp
    else:
        return "O que veio do meu form : " +request.form['nome']

@app.route("/sobre")
def sobre():
    return "<h2>Sobre</h2>"


@app.route("/noticia/<noticia_slug>")
def noticia(noticia_slug):
    return "Noticia: " +noticia_slug
  