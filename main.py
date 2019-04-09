import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)
@app.route('/create/', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            amount = int(request.form['amount'])
        except ValueError:
            return render_template('create.jinja2', error = 'Enter a True Value')
        try:
            donor = Donor.get(Donor.name == request.form['name'])
        except Donor.DoesNotExist:
            return render_template('create.jinja2', error = 'Donor Does Not Exist')
        else:
            Donation(donor=donor, value=amount).save()
            return redirect(url_for('all'))
    else:
        return render_template('create.jinja2')



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='127.0.0.1', port=port, debug=True)

    # if request.method == 'POST':
    #     donor = Donor.get(Donor.name == request.form['name'])
    #     amount = int(request.form['amount'])
    #     Donation(donor=donor, value=amount).save()
    #     return redirect(url_for('all'))
    # else:
    #     return render_template('create.jinja2')


    # if request.method == 'POST':
    #     try:
    #         amount = int(request.form['amount'])
    #     except ValueError:
    #         return render_template('create.jinja2', error = 'Enter a True Value')
    #     try:
    #         donor = Donor.get(Donor.name == request.form['name'])
    #     except Donor.DoesNotExist:
    #         return render_template('create.jinja2', error = 'Donor Does Not Exist')
    #     else:
    #         Donation(donor=donor, value=amount).save()
    #         return redirect(url_for('all'))
    # else:
    #     return render_template('create.jinja2')
