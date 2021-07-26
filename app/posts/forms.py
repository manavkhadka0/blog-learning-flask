



from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField("Title",validators=[DataRequired(),Length(min=5)])
    content = TextAreaField("Content",validators=[DataRequired(),Length(min=5)])
    submit = SubmitField('Post')