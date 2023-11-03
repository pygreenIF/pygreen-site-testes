from flask import Flask, render_template, redirect, request, flash
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='labinfo',
    database='auth'
)

@app.route('/')
def home():
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM Pessoa")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('home.html', data = fetchdata)


@app.route('/registrar')
def entrar():
    return render_template('registrar.html')

@app.route("/registrar", methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    usuario = request.form.get('nome')
    senha = request.form.get('senha')
    cur = db.cursor(dictionary=True)
    cur.execute(f"SELECT * FROM Pessoa WHERE email='{email}'")
    fetchdata = cur.fetchall()
    
    if(fetchdata):
        raise Exception("Ei, deu erro... Já tem esse email ó")
    else:
        post = f"INSERT INTO Pessoa (tipoID, email, nome, senha) VALUES (1, '{email}', '{usuario}', '{senha}')"
        cur.execute(post)
        cur.close()
        db.commit()
        return redirect('/acesso')
    
@app.route("/acesso")
def acesso():
    return render_template('acesso.html')

if __name__ == '__main__':
    app.run(debug=True)