from flask import current_app
from flask_mail import Message, Mail, email_dispatched
from flask_babel import gettext, ngettext, lazy_gettext
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from myapp.main import main
from myapp import mail

users = [
  {'username' : 'liujun', 'password' : generate_password_hash('111111')},
  {'username' : 'admin', 'password' : generate_password_hash('222222')}
]

hello = lazy_gettext(u'Hello World')
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
  for user in users:
    if user['username'] == username:
      return user['password']

@auth.verify_password
def verify_password(username, password):
  for user in users:
    if user['username'] == username:
      if check_password_hash(user['password'], password):
        return True
  return False

@main.route('/')
@auth.login_required
def index():
  return '<h1>This this main index</h1><p>Hello, %s!</p>' % auth.username()

def mail_send(message, app):
  print 'Message %s is sent successfully' % message.subject

email_dispatched.connect(mail_send)

@main.route('/mail')
def send_mail():
  msg = Message('Hello', sender=('liujun', '13011024902@163.com'),
    recipients=['13011024902@163.com'])
  msg.html = '<h1>Hello World</h1>'
  with current_app.open_resource('pygments_ext.py', 'rb') as fp:
    msg.attach('pygemnts_ext.py', 'text/python', fp.read(), disposition='inline')
  mail.send(msg)
  return 'Successful'

@main.route('/trans')
@main.route('/trans/<int:num>')
def translate(num=None):
  if num is None:
    return gettext(u'No users')
  return ngettext(u'%(num)d user', u'%(num)d users', num)

@main.route('/lazy')
def lazy():
  return unicode(hello)