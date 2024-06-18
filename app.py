from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User
from forms import RegistrationForm
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key='e98ecfcbcac9988e748e82151c28086b8dc77da939a829bd0a15ef4b75a265d7'
app.config ['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/daily_diving/')
def daily_diving():
    return render_template('daily.html')


@app.route('/excursions/')
def excursions():
    excursions= [
        {"title":"Daily diving", "price":"45$ p.p.", "img":"/static/images/2.png", "address":"/daily/",
         "description":"Full day trip. 2 diving, transfer, equipment, lunch, soft drinks"},
        {"title": "Wreck diving. Salem Express", "price": "150$ p.p.", "img":"/static/images/3.png", "address":"#",
         "description": "Full day trip. 2 diving (wreck, coral reef), transfer, equipment, lunch, soft drinks"},
        {"title": "Night diving", "price": "60$ p.p.", "img":"/static/images/4.png", "address":"#",
         "description": "Full day trip. 1 diving, transfer, equipment"}
    ]
    return render_template('excursions.html', excursions=excursions)


@app.route('/daily/')
def daily():
    daily= [
        {"title":"Daily diving", "price":"45$ p.p.", "img":"/static/images/2.png",
         "description":"Full day trip. Starts from 08.00 a.m. and finished at 03.30 p.m. 2 diving on different coral reefs. Transfer from hotel and back, diving equipment, lunch on the boat, soft drinks during trip are included"}
            ]
    return render_template('daily.html', daily=daily)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('name', 'email')
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route ('/register/', methods = ['GET', 'POST'])
def register():
    form=RegistrationForm()
    if request.method=='POST' and form.validate():
        username=form.username.data
        surname=form.surname.data
        email=form.email.data
        password=form.password.data
        new_user=User(username=username, surname=surname, email=email, password=password)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        success_msg="Registartion is successful"
        return success_msg
    else:
        return render_template('register.html', form=form)

@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('OK')




if __name__=='__main__':
    app.run()
