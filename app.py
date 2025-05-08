from flask import Flask, render_template

import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/page")
def page():
    x1, y1 = random.randint(1, 400), random.randint(1, 400)
    x2, y2 = random.randint(1, 400), random.randint(1, 400)
    return render_template("page.html", x1=x1, y1=y1, x2=x2, y2=y2)


if __name__ == "__main__":
    app.run(debug=True)
