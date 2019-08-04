"""
views imports app and models; these don't import views
"""
# -*- coding: utf-8 -*-

from flask import render_template
from app import app
import pandas as pd
import json


@app.route('/', methods=['GET'])
def index():
    df = pd.read_csv("static/footprintnetwork.csv")
    chart_data = json.dumps(df.to_dict(orient='records'), indent=2)
    data = {'chart_data':chart_data }
    return render_template('index.html', data=data)
