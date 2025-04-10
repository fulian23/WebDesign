from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect

from app import routes
from app.api import search

from db_config import Config
from app.models import db, Users

from app.forms import LoginForm




app = Flask(__name__)
app.secret_key = 'test'
csrf = CSRFProtect(app)
app.register_blueprint(routes.news)
app.register_blueprint(search.search)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config.from_object(Config)
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Users, int(user_id))


@app.route('/login', methods=['GET', 'POST'])
async def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():  # 自动触发所有验证器
        user = db.session.query(Users).filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('用户名或密码错误')
    for field, errors in form.errors.items():
        for error in errors:
            flash(error)
    return render_template('login.html',form=form)

@app.route('/register', methods=['GET', 'POST'])
async def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        if Users.query.filter_by(username=form.username.data).first():
            flash('用户名已存在')
            return redirect(url_for('register'))
        user = Users(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('login'))
    for field, errors in form.errors.items():
        for error in errors:
            flash(error)
    return render_template('register.html',form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run()