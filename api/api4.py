from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"""
    <a href="/"hobbiler</a>
    """

@app.route("/hobbiler")
def hobbiler():
    return """
    <h1>Hobbilərim</h1>
    <ul>
        <li>Kitab oxumaq</li>
        <li>Flask öyrənmək</li>
        <li>Musiqi dinləmək</li>
    </ul>
    <a href="/">Geri qayıt</a>
    """

if __name__ == "__main__":
    app.run(port=5016, debug=True)
