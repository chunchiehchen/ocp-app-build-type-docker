import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "hello,world"

@app.route('/hello')
def hello():
    return 'world'

if __name__ == "__main__":
    app.run()