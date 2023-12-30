from flask import Flask, request, render_template
from app.metmuseum import bp
import pandas as pd

@bp.route("/metmuseum")
def show_met_api():
    return render_template("metmuseum/metmuseum.html")