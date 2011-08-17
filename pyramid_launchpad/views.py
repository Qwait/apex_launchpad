from pyramid.httpexceptions import HTTPFound
from pyramid.i18n import TranslationString as _
from pyramid.view import view_config

from pyramid_apex.lib.flash import flash
from pyramid_apex.lib.apex import apex_settings
from pyramid_apex.lib.apex import create_user
from pyramid_apex.models import AuthUser
from pyramid_apex.models import DBSession

from pyramid_launchpad.models import ForeignKeyProfile
from pyramid_launchpad.forms import LandingForm

def referrer_update(user, refer_id):
    try:
        fkp = DBSession.query(ForeignKeyProfile). \
                  filter(ForeignKeyProfile.user_id==refer_id).one()
    except:
        fkp = ForeignKeyProfile(user_id = refer_id, score = 0)
    fkp.score = fkp.score + 1
    DBSession.merge(fkp)

    try:
        fkp = DBSession.query(ForeignKeyProfile). \
                  filter(ForeignKeyProfile.user_id==user.id).one()
    except:
        fkp = ForeignKeyProfile(user_id = user.id, score = 0)
    fkp.parent_id = refer_id
    DBSession.merge(fkp)

    DBSession.flush()

def landing(request):
    form = []
    action = 'index'
    if request.session.get('id'):
        action = 'social'
    else:
        form = LandingForm(request.POST)
        if request.method == 'POST' and form.validate():
            group = apex_settings('default_user_group')
            user = create_user(email = request.POST['email'], \
                               group = group)
            flash(_('Thanks'))
            request.session['id'] = user.id
            if request.matchdict.get('refer_id'):
                referrer_update(user, request.matchdict['refer_id'])
            return HTTPFound(location='/thanks')

    return {'form': form, 'action': action}

def thanks(request):
    return {'action':'thanks'}
