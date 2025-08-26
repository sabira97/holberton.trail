from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1> ebjbnelb </h1>
    <p style="color:MediumSeaGreen;">Ut wisi enim...</p>
    <a href="/hobbiler">Hobbiler</a>
    <a href="/kitablar">Kitablar</a>
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
