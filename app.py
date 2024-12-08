from os import name

from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return ("<h1>Lab 8: Deploy by Jenkins"
            "Задача: задеплоить личный проект с GitHub с помощью Jenkins.</p>")

if name == "main":
    app.run(debug=True)
