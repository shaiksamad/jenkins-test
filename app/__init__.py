from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, this application is auto deployed"
  

if __name__ == "__main__":
    app.run(port=1234)
