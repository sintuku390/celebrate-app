
from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

html_page = """<!DOCTYPE html>
<html>
<head>
<title>Celebration App</title>
<h1>App Running!</h1>
</head>
<body>
Welcome!
</body>
</html>"""

@app.route("/", methods=["GET", "POST"])
def home():
    username = None
    if request.method == "POST":
        username = request.form.get("username")
    return render_template_string(html_page, username=username)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
