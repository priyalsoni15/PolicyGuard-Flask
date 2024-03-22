import re

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
async def render_index(name = None):
    return render_template(
        "index.html",
        name=name
    )

async def render_template_async(template_name_or_list, **context):
    return render_template(template_name_or_list, **context)

if __name__ == "__main__":
    app.run(debug=True)