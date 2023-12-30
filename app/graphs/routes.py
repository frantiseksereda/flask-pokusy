from flask import Flask, request, render_template
from app.graphs import bp
import pandas

@bp.route("/graphs")
def show_graphs():

    return render_template("graphs/graphs.html")
