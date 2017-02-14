# coding: utf8

from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, DateField, BooleanField,
                            SelectField, SelectMultipleField, TextAreaField,
                            RadioField, IntegerField, DecimalField, SubmitField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
 
class MyForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    # Text Field类型，文本输入框，必填，用户名长度为4到25之间
    username = StringField('Username', validators=[Length(min=4, max=25)])
 
    # Text Field类型，文本输入框，Email格式
    email = StringField('Email Address', validators=[Email()])
 
    # Text Field类型，密码输入框，必填，必须同confirm字段一致
    password = PasswordField('Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
 
    # Text Field类型，密码输入框
    confirm = PasswordField('Repeat Password')
 
    # Text Field类型，文本输入框，必须输入整型数值，范围在16到70之间
    age = IntegerField('Age', validators=[NumberRange(min=16, max=70)])
 
    # Text Field类型，文本输入框，必须输入数值，显示时保留一位小数
    height = DecimalField('Height (Centimeter)', places=1)
 
    # Text Field类型，文本输入框，必须输入是"年-月-日"格式的日期
    birthday = DateField('Birthday', format='%Y-%m-%d')
 
    # Radio Box类型，单选框，choices里的内容会在ul标签里，里面每个项是(值，显示名)对
    gender = RadioField('Gender', choices=[('m', 'Male'), ('f', 'Female')],
                                  validators=[DataRequired()])
 
    # Select类型，下拉单选框，choices里的内容会在Option里，里面每个项是(值，显示名)对
    job = SelectField('Job', choices=[
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('engineer', 'Engineer'),
        ('lawyer', 'Lawyer')
    ])
 
    # Select类型，多选框，choices里的内容会在Option里，里面每个项是(值，显示名)对
    hobby = SelectMultipleField('Hobby', choices=[
        ('swim', 'Swimming'),
        ('skate', 'Skating'),
        ('hike', 'Hiking')
    ])
 
    # Text Area类型，段落输入框
    description = TextAreaField('Introduction of yourself')
 
    # Checkbox类型，加上default='checked'即默认是选上的
    accept_terms = BooleanField('I accept the Terms of Use', default='checked',
                                validators=[DataRequired()])
 
    # Submit按钮
    submit = SubmitField('Register')