from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2> Aynur oxuyur guyaaa</h2>
    <a href="/etrafinda">Etrafinda</a>
    """

@app.route("/etrafinda")
def etrafinda():
    return """
    <h1>Sabira oxuyur</h1>
"""

if __name__ == "__main__":
    app.run(debug=True)