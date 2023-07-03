import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, Clever Cloud Script Bot Is Running!'

os.system("$START_CMD")
