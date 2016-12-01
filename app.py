# -*- coding: utf-8 -*-

import pandas as pd
#from shapely.geometry import Point, shape

from flask import Flask
from flask import render_template
import json

data_path = './input/'
DEV=True

#if DEV:
#  import modules.rootUtils as rootutils



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
  cleanDB = [
              {"var1":1.0,"var2":1.8,"var3":2.9},
              {"var1":1.2,"var2":2.0,"var3":3.0},
              {"var1":0.8,"var2":2.2,"var3":3.1},
            ]
  return json.dumps(cleanDB) 



if __name__ == "__main__":
#    app.run(host='0.0.0.0',port=5000,debug=True)
  app.run(debug=DEV)
#  get_data()