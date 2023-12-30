from flask import Flask, request, render_template
from app.metmuseum import bp
import pandas as pd
import http.client
import json


def get_met_departments_table():
    conn = http.client.HTTPSConnection("collectionapi.metmuseum.org")
    payload = ''
    headers = {}
    conn.request("GET", "/public/collection/v1/departments", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_data = json.loads(data)
    departments_df = pd.DataFrame(json_data['departments'])
    departments_table_html = departments_df.to_html()
    return departments_table_html
    

@bp.route("/metmuseum")
def show_met_api():
    return render_template("metmuseum/metmuseum.html", departments=get_met_departments_table())