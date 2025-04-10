from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[
        DataRequired(message="用户名不能为空"),  # 必填验证
        Length(min=2, max=6, message="用户名长度需在2-6字符")
    ])
    password = PasswordField('密码', validators=[
        DataRequired(message="密码不能为空"),
        Length(min=6, max=15, message="密码长度需在6-15字符")
    ])
    submit = SubmitField('登录')
class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[
        DataRequired(message="用户名不能为空"),  # 必填验证
        Length(min=2, max=6, message="用户名长度需在2-6字符")
    ])
    password = PasswordField('密码', validators=[
        DataRequired(message="密码不能为空"),
        Length(min=6, max=15, message="密码长度需在6-15字符")
    ])
    submit = SubmitField('登录')