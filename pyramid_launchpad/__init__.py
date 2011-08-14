from pyramid_apex.interfaces import IPyramidApex

from pyramid_launchpad.exceptions import MessageException
from pyramid_apex.interfaces import IPyramidLaunchpad
from pyramid_apex.interfaces import PyramidLaunchpadImplementation
from pyramid_launchpad.views import landing
from pyramid_launchpad.views import thanks

def includeme(config):
    settings = config.registry.settings

    config.registry.registerUtility(PyramidLaunchpadImplementation, IPyramidLaunchpad)

    if not config.registry.queryUtility(IPyramidApex):
        raise MessageException('Pyramid Apex isn\'t setup')
    
    config.add_subscriber('pyramid_launchpad.lib.subscribers.add_renderer_globals', 'pyramid.events.BeforeRender')

    config.add_static_view('pyramid_launchpad/static', 'pyramid_launchpad:static')

    if not settings.get('mako.directories'):
        config.add_settings({'mako.directories': ['pyramid_launchpad:templates']})

    render_template = getattr(settings, 'launchpad.launchpad_template', 'pyramid_launchpad:templates/launchpad_template.mako')

    config.add_route('pyramid_launchpad_landing', '/')
    config.add_view(landing, route_name='pyramid_launchpad_landing', renderer=render_template)

    config.add_route('pyramid_launchpad_thanks', '/thanks')
    config.add_view(thanks, route_name='pyramid_launchpad_thanks', renderer=render_template)    
    
    
    '''
    title
    meta_description
    meta_keywords
    
    form_image
    background_image
    
    alert_message
    blurb
    
    favicon
    
    google analytics
    
    og:title
    og:type
    og:url
    og:image
    og:site_name
    fb:admins
    
    facebook app id
    '''