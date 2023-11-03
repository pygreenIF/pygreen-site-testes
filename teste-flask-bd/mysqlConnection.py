from flask import Flask, render_template, redirect, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "super secret key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pygreen2023'
app.config['MYSQL_DB'] = 'auth'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
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
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Pessoa")
    fetchdata = cur.fetchall()
    
    registro = 0
    for users in fetchdata:
        if email == users[2]:
            flash('Já existe um cadastro com esse email')
            registro+=1
            return redirect('/registrar')
        if usuario == users[3]:
            flash('Esse nome de usuário não está disponível')
            registro+=1
            return redirect('/registrar')
    if registro == 0:
        post = f"INSERT INTO Pessoa (tipoID, email, nome, senha) VALUES ({1}, '{email}', '{usuario}', '{senha}')"
        cur.execute(post)
        mysql.connection.commit()
        return redirect('/acesso')
    cur.close()
    
@app.route("/acesso")
def acesso():
    return render_template('acesso.html')

if __name__ == '__main__':
    app.run(debug=True)