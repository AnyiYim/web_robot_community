from wtforms import StringField, IntegerField, FileField
from wtforms.validators import DataRequired
from views.form import Base


class LoginForm(Base):
    name = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])


class SignInForm(Base):
    name = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])
    phone = StringField(validators=[DataRequired()])
    role = StringField()


class BindUserForm(Base):
    id = IntegerField(validators=[DataRequired()])
    uid = IntegerField(validators=[DataRequired()])


class RoleForm(Base):
    id = IntegerField(validators=[DataRequired()])
    day = IntegerField(validators=[DataRequired()])


class CallBackForm(Base):
    id = IntegerField(validators=[DataRequired()])
    call = StringField(validators=[DataRequired()])


class UploadForm(Base):
    pic = FileField(validators=[DataRequired()])
