from flask import render_template, request, Blueprint, flash, redirect, url_for
from main.forms import DataEntry, DataEntryUpdate
from main.models import Another
from main import db


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    another = Another.query.all()
    return render_template('home.html', another=another)


@main.route("/new", methods=['GET', 'POST'])
def new():
    form = DataEntry()
    if form.validate_on_submit():
        data = Another(title=str(form.title.data), grouping=form.grouping.data)
        db.session.add(data)
        db.session.commit()
        flash('Your data has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('dataEntry.html', title='New Data', form=form)


@main.route("/data/<int:id>/delete", methods=['POST'])
def delete(id):
    record = Another.query.get(id)
    db.session.delete(record)
    db.session.commit()
    flash('Your record has been deleted!', 'success')
    return redirect(url_for('main.home'))

    
@main.route("/data/<int:id>/update", methods=['GET', 'POST'])
def update(id):
    record = Another.query.get(id)
    form = DataEntryUpdate()
    if form.validate_on_submit():
        record.title = str(form.title.data)
        record.grouping = form.grouping.data
        db.session.commit()
        flash('Your data has been updated!', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.title.data = record.title
        form.grouping.data = record.grouping
    return render_template('dataEntry.html', title='Update Data', form=form, legend='Update Post')