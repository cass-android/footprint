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

    months = ['Jan','Feb','Mar','Apr','May','Jun',
     'Jul','Aug','Sep','Oct','Nov','Dec', ' Jan', ' Feb', ' Mar', ' Apr', ' May', ' Jun']

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15,16,17,18]

    df = pd.read_csv("static/footprintnetwork.csv")

    df2 = pd.DataFrame({'month':months, 'value':values})

    chart_data = json.dumps(df.to_dict(orient='records'), indent=2)
    ylabel_data = json.dumps(df2.to_dict(orient='records'), indent=2)

    data = {'chart_data':chart_data, 'ylabel_data':ylabel_data }

    return render_template('index.html', data=data)
