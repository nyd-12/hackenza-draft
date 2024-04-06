from flask import Flask, render_template, redirect, url_for
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Connecting to DB
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///our_data.db"
db.init_app(app)


class USER_DETAIL(db.Model):
    __tablename__ = "user_detail"
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    roles = db.Column(db.String(120), nullable=False)


class JOURNALS(db.Model):
    __tablename__ = "journals"
    j_email = db.Column(db.String(120), nullable=False)
    j_dop = db.Column(db.String(20), nullable=False)
    j_nat_inat = db.Column(db.String(120), nullable=False)
    j_ranking = db.Column(db.Integer, nullable=False)
    j_broad_area = db.Column(db.String(120), nullable=False)
    j_con_name = db.Column(db.String(120))
    j_impf = db.Column(db.String(120), nullable=False)
    j_pap_tit = db.Column(db.String(120), nullable=False)
    j_doi = db.Column(db.String(120), nullable=False, primary_key=True)
    j_authors = db.Column(db.String(200), nullable=False)
    j_volume = db.Column(db.String(120), nullable=False)
    j_issue = db.Column(db.String(120), nullable=False)
    j_page_n = db.Column(db.String(120), nullable=False)
    j_publisher = db.Column(db.String(120), nullable=False)


class CONFERENCE(db.Model):
    __tablename__ = "conference"
    c_email = db.Column(db.String(120), nullable=False)
    c_date = db.Column(db.Integer, primary_key=True)
    c_nat = db.Column(db.String(120), nullable=False)
    c_corerank = db.Column(db.Integer, nullable=False)
    c_pap_tit = db.Column(db.String(120), nullable=False)
    c_short_name = db.Column(db.String(120), nullable=False)
    c_con_location = db.Column(db.String(120), nullable=False)
    c_full_name = db.Column(db.String(120), nullable=False)
    c_url = db.Column(db.String(120), nullable=False, primary_key=True)
    c_authors = db.Column(db.String(200), nullable=False)
    c_volume = db.Column(db.String(120), nullable=False)
    c_issue = db.Column(db.String(120), nullable=False)
    c_page_n = db.Column(db.String(120), nullable=False)
    c_publisher = db.Column(db.String(120), nullable=False)


with app.app_context():
    db.create_all()


# db.create_all()

@app.route('/')
def login_page():
    return render_template("LoginPage.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process the form data here
        print(form.email.data)
        print(form.password.data)

        ##check in the data base##

        # if passed then the next line
        # if admin then pass then
        # return redirect(url_for('admin_page'))
        # else
        return redirect(url_for('home_page'))
        # else add the user in the database----------ye alag se function hoga...
        # else show unauthorised access
    return render_template('login.html', form=form)


@app.route('/home')
def home_page():
    return render_template("HomePage.html")


@app.route('/admin')
def admin_page():
    return render_template("AdminPage.html")


@app.route('/admin_publication')
def admin_pub_page():
    return render_template("AdminPublicationPage.html")


@app.route('/entries')
def entries():
    return render_template("EntriesPage.html")


@app.route('/publication', methods=['GET', 'POST'])
def publication():
    return render_template("PublicationPage.html")


@app.route('/unauthorised')
def unauthorized():
    return render_template("UnauthorizedAccess.html")


@app.route('/journal')
def journal_page():
    return render_template("JournalPage.html")


@app.route('/conference')
def conference():
    return render_template("ConferencePage.html")


@app.route('/publication_edit')
def pub_edit_page():
    return render_template("PublicationEditPage.html")


if __name__ == "__main__":
    app.run(debug=True)
