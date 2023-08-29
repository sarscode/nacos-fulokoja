from flask import render_template, redirect, url_for
from app.site import blueprint
from app.site.forms import SubscribeForm


@blueprint.route('/')
def home():
    form = SubscribeForm()
    if form.validate_on_submit():
        return redirect(url_for('site_blueprint.subscribe'))
    return render_template('site/index.html', form=form)
