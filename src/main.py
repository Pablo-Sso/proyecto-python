import pandas as pd
from flask import Flask
app = Flask(__name__)

# esto es un comentario
def suma(a,b):
  c=1+1
  return a+b+c

# este es el endpoint
@app.route("/")
def hello():
    res = suma(3,2)
    # un comentario
    return "Hello World! %s" % (res)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
