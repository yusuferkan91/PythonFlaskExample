from wtforms import SelectField
from flask_wtf import FlaskForm


class Form(FlaskForm):
    kur_isim = SelectField("isim", choices=[])
    kur_deger = SelectField("deger", choices=[])
