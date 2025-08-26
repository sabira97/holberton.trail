from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"""
    <h1>Sadə Blog</h1>
    <a href="/postlar">Postlara bax</a>
    """

@app.route("/postlar")
def postlar():
    return """
    <h1>Blog Postları</h1>
    <ul>
        <li>Flask-in esaslari</li>
        <li>Python ile veb proqramlaşdirma</li>
        <li>API-lerle işlemek</li>
    </ul>
    <a href="/">Ana sehife</a>
    """

if __name__ == "__main__":
    app.run(port=5021, debug=True)
