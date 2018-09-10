from flask import Flask
from flask import request, render_template


app = Flask(__name__)


@app.route("/home")
def show_home():
    """renders home.html"""

    return render_template("home.html")


@app.route("/random")
def show_random():
    """renders random.html"""

    return render_template("random.html")


@app.route("/not-random")
def show_not_random():
    """renders not-random.html"""

    return render_template("not-random.html")


def return_random_dad_joke():
    """generates random dad joke"""


def returns_user_guided_dad_joke():
    """generates dad joke from user input"""

    


if __name__ == "__main__":
    app.run(debug=True)