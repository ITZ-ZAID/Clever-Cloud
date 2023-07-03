import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, Telethon Music Bot Is Running!'

os.system("git clone $REPO_URL ok && cd ok && pip3 install -r requirements && $START_CMD")
