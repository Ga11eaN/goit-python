from flask.helpers import flash
from werkzeug.utils import redirect
from app import app,db
from flask import render_template, url_for
from app.forms import ContactForm
from app.models import Contact


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Main menu")


@app.route("/new_contact_list", methods=["GET", "POST"])
def create_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            contact_name = form.contact_name.data,
            phone = form.phone.data,
            mail = form.mail.data,
            address = form.address.data,
            birthday = form.birthday.data
            )
        db.session.add(contact)
        db.session.commit()
        flash(f"New contact {form.contact_name.data} created!")
        return redirect(url_for("index"))
    return render_template("new_contact.html", title="Create new contact", form=form)

@app.route('/view_contacts')
def view_contacts():
    contacts = Contact.query.all()
    return render_template('contacts.html', title = 'Contact list', contacts = contacts)
    
@app.route('/contacts/<contact_name>')
def contact(contact_name):
    contact = Contact.query.filter_by(contact_name = contact_name).first_or_404()
    return render_template('contact.html', title = 'Contact', contact = contact)