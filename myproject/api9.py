from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "Xoş gəlmisiniz!"

if __name__ == "__main__":
    app.run()