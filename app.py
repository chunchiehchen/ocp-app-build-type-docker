import os,datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "hello,world"

@app.route('/now')
def hello():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    app.run()
