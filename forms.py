from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,SubmitField
from wtforms.validators import DataRequired, Length

class SignUpForm(FlaskForm):
    gender = SelectField("מין", choices=[('זכר','זכר'),('נקבה','נקבה')], validators=[DataRequired('שדה זה הוא שדה חובה')])
    first_name = StringField('שם פרטי', validators=[DataRequired('שדה זה הוא שדה חובה')])
    last_name = StringField('שם משפחה', validators=[DataRequired('שדה זה הוא שדה חובה')])
    date_day = SelectField(choices=[('', 'יום')]+[(i, i) for i in range(1, 32)])
    date_year = SelectField(choices=[('', 'שנה')]+[(i, i) for i in range(1940, 2024)])
    date_month = SelectField(choices=[('', 'חודש')] + [(i, i) for i in range(1, 13)])
    father_name = StringField('שם האב', validators=[DataRequired('שדה זה הוא שדה חובה')])
    mother_name = StringField('שם האם', validators=[DataRequired('שדה זה הוא שדה חובה')])
    city_born = StringField('מקום לידה', validators=[DataRequired('שדה זה הוא שדה חובה')])
    citizen = StringField('לאום', validators=[DataRequired('שדה זה הוא שדה חובה')])
    id = StringField('מספר תעודת זהות', validators=[DataRequired('שדה זה הוא שדה חובה'),Length(9,9,'חייב להיות 9 ספרות')])
    submit = SubmitField("אישור פרטים")
    