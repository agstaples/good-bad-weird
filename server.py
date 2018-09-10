from flask import Flask
from flask import request, render_template


app = Flask(__name__)


@app.route("/home")
def show_homescreen():
    """renders home.html"""

    return render_template("home.html")





if __name__ == "__main__":
    app.run(debug=True)