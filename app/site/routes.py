from flask import render_template, redirect, url_for
from app import db
from app.site import blueprint
from app.site.forms import SubscribeForm
from app.site.models import Subscriber


@blueprint.route('/')
def home():
    form = SubscribeForm()
    if form.validate_on_submit():
        return redirect(url_for('site_blueprint.subscribe'))
    return render_template('site/index.html', form=form)


@blueprint.route('/about')
def about():
    form = SubscribeForm()
    if form.validate_on_submit():
        return redirect(url_for('site_blueprint.subscribe'))
    return render_template('site/about.html', form=form)


@blueprint.route('/subscribe', methods=['POST'])
def subscribe():
    form = SubscribeForm()
    if form.validate_on_submit():
        subscriber = Subscriber.query.filter_by(
            email_address=form.email_address.data).first()
        if subscriber:
            return redirect(url_for('site_blueprint.home'))
        subscriber = Subscriber(email_address=form.email_address.data)
        db.session.add(subscriber)
        db.session.commit()
    return redirect(url_for('site_blueprint.home'))
