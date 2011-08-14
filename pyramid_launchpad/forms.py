from wtforms import TextField
from wtforms import validators

from pyramid_apex.lib.form import ExtendedForm

class LandingForm(ExtendedForm):
    email = TextField('Email', [validators.Email(), validators.Required()])
    