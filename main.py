from flask import Flask
import os


app = Flask(__name__)

@app.route("/recieve")
def recieve():
  return "echo Hello, World!"

@app.route("/send")
def send():
  return "send Router"


if __name__ == "__main__":
  app.run(port = 5000)
