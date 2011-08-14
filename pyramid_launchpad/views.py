from pyramid.httpexceptions import HTTPFound
from pyramid.i18n import TranslationString as _
from pyramid.view import view_config

from pyramid_apex.lib.flash import flash

from pyramid_launchpad.forms import LandingForm

def landing(request):
    form = LandingForm(request.POST)

    if request.method == 'POST' and form.validate():
        flash(_('Thanks'))
        return HTTPFound(location='/')

    return {'form': form}

def thanks(request):
    return {}