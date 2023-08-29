from flask import render_template
from app.site import blueprint


@blueprint.route('/')
def home():
    return render_template('site/index.html')
