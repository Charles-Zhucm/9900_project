from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    acc_name = request.form.get("acc")
    password = request.form.get("password")
    if acc_name == "charles" and password == "666":
        return "Success!!"
    else:
        return render_template("login.html", msg="Failed!! ReEnter plz")


if __name__ == '__main__':
    app.run()
