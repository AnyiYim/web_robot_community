from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from views.form import Base


class CallInForm(Base):
    id = IntegerField(validators=[DataRequired()])
    msg = StringField(validators=[DataRequired()])


