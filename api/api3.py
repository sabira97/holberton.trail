from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Əlaqə</h1>
    <p>Email: sabira@example.com</p>
    <a href="/">Geri qayıt</a>
    """


if __name__ == "__main__":
    app.run(port=5016, debug=True)
