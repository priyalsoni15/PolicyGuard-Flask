import re

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def render_index(name = None):
    return render_template(
        "index.html",
        name=name
    )

if __name__ == "__main__":
    app.run(debug=True)