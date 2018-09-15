from flask import Flask, request, render_template, jsonify, session
from markov import random_forward_markov, multi_directional_markov


app = Flask(__name__)

app.secret_key = "V*jL???Lu?{"


@app.route("/")
def show_home():
    """renders home.html"""

    return render_template("home.html")


@app.route("/set_num_words.json", methods=["POST"])
def set_num_words():
    """saves num_words in session based on user unput"""

    num_words_str = request.form.get("num_words")

    # getting rounded integer from string
    # (string numbers have decimal places because of slider scale)
    num_words = int(round(float(num_words_str)))

    session["num_words"] = num_words

    return str(num_words)


@app.route("/get_random_joke.json")
def return_random():
    """returns random dad joke"""

    if session.get("num_words"):
        num_words = session.get("num_words")
    else:
        num_words = 2

    response = random_forward_markov(num_words)

    return response


@app.route("/get_not_random_joke.json", methods=["POST"])
def return_not_random():
    """returns dad joke based on user click"""

    if session.get("num_words"):
        num_words = session.get("num_words")
    else:
        num_words = 2

    user_input = request.form.get("user_input")
    # joke_class being used to set class for each successive joke
    joke_class = request.form.get("joke_class")

    # index marker is index of word in next joke to be rendered in red
    joke, index_marker = multi_directional_markov(user_input, num_words)

    response = {"joke": joke, "joke_class": joke_class, "index_marker": index_marker}

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=False)