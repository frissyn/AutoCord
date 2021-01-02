from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField

from wtforms.validators import Length
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired


class SubmissionForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired(), Length(min=2, max=64)])
    prefix = StringField(
        "Bot Prefix", validators=[DataRequired(), InputRequired(), Length(min=2, max=4)]
    )
    description = TextAreaField(
        "Paste Code", validators=[DataRequired(), InputRequired()]
    )

    submit = SubmitField("Confirm Submission")
