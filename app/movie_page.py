import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/')
def movie_page():
    return render_template('movie_page.html')

if __name__ == "__main__":
    app.run(debug=True)