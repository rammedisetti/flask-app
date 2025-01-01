from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def index():
    # Serve the HTML file
    return render_template('test.html')