from wtforms import TextField
from wtforms import validators

from pyramid.i18n import TranslationString as _

from pyramid_apex.models import AuthUser
from pyramid_apex.lib.form import ExtendedForm

class LandingForm(ExtendedForm):
    email = TextField('Email', [validators.Email(), validators.Required()])

    def validate_email(form, field):
        if AuthUser.get_by_email(field.data) is not None:
            raise validators.ValidationError(_('Sorry that email already exists.'))
    
