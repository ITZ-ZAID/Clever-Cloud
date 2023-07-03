#!/bin/bash
git clone $REPO_URL ok && cd ok && pip3 install -U -r requirements.txt
python3 app.py & $START_CMD
