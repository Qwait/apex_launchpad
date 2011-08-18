from wtforms import TextField
from wtforms import validators

from pyramid.i18n import TranslationString as _

from apex.models import AuthUser
from apex.lib.form import ExtendedForm

class LandingForm(ExtendedForm):
    email = TextField('Email', [validators.Email(), validators.Required()])

    def validate_email(form, field):
        if AuthUser.get_by_email(field.data) is not None:
            raise validators.ValidationError(_('Sorry that email already exists.'))
    
