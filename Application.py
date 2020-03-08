from flask import Flask 
from flask import render_template
from flask import request
from datetime import datetime as dt
import os
import re

now=dt.today()
info={}

app=Flask(__name__)
@app.route('/')
def main():
    return render_template('Mainpage.html')
app.run(debug=True)
