from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"""
    <h1 style="color:purple;">Salam, Flask!</h1>
    <p>Bu, sade veb sehife nümunesidir.</p>
    <a href="/sayfa1">Sehife 1</a> | <a href="/sayfa2">Sehife 2</a>
"""

@app.route("/sayfa1")
def sayfa1():
    return """
    <h1>Sehife 1</h1>
    <p>Bu, birinci sehifedir.</p>
    <a href="/">Ana sehife</a>
    """

@app.route("/sayfa2")
def sayfa2():
    return """
    <h1>Sehife 2</h1>
    <p>Bu, ikinci sehifedir.</p>
    <a href="/">Ana sehife</a>
    """

if __name__ == "__main__":
    app.run(port=5023, debug=True)