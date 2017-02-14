from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required
from myapp.admin import admin
from myapp.admin.forms import MyForm, RegisterForm
from myapp.admin.models import User
from myapp import login_manager

login_manager.login_view = 'admin.login'
login_manager.login_message = 'Unauthorized User'
login_manager.login_message_category = 'info'

users = [
  {'username' : 'liujun', 'password' : '111111'},
  {'username' : 'admin', 'password' : '222222'}
]

def query_usser(username):
  for user in users:
    if user['username'] == username:
      return user

@login_manager.user_loader
def user_loader(username):
  print username
  if query_usser(username) is not None:
      user = User()
      user.id = username
      return user


@admin.route('/')
@login_required
def index():
  return render_template('admin/index.html')

@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        # if form.user.data == 'admin':
        if form.data['user'] in map(lambda x: x['username'], users):
            user = User()
            user.id = form.data['user']
            login_user(user)
            print request.args.get('next')
            return redirect(url_for('admin.index'))
        else:
            flash('login error', 'error')
            return redirect(url_for('admin.login'))
    return render_template('admin/login.html', form=form)

@admin.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('User "%s" registered successfully! Please login.' % form.username.data)
        login_form = MyForm()
        return render_template('admin/login.html', form=login_form)
 
    return render_template('admin/register.html', form=form)