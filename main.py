from flask import Flask, render_template, url_for, flash, redirect
from forms import NewCustomerForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1541628f14da600e2c2f5a807019390c'


@app.route("/")
@app.route("/home/")
def home():
    return render_template('home.html')


@app.route("/addnewresult/")
def add_result():
    return render_template('result.html')


@app.route("/addnew/", methods=["POST", "GET"])
def add():
    form = NewCustomerForm()
    if form.validate_on_submit():
        print(form.errors)
        return redirect(url_for('add_result'))
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=3000)