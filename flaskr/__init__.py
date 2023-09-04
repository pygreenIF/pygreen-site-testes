from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/sobre")
def sobre():
    return "sobre"
    
if __name__ == "__main__":
    app.run(debug=True)