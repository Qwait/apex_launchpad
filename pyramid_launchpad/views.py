from pyramid.httpexceptions import HTTPFound
from pyramid.i18n import TranslationString as _
from pyramid.view import view_config

from pyramid_apex.lib.flash import flash

from pyramid_launchpad.forms import LandingForm
from pyramid_launchpad.lib.launch import launch_settings

def landing(request):
    form = LandingForm(request.POST)
    action = 'index'
    if request.session.get('id'):
        action = 'social'
    else:
        if request.method == 'POST' and form.validate():
            request.session['id'] = 1
            flash(_('Thanks'))
            return HTTPFound(location='/thanks')

    return {'form': form, 'action': action}

def thanks(request):
    return {'action':'thanks'}
