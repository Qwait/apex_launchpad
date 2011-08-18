from apex.interfaces import IApex

from apex_launchpad.exceptions import MessageException
from apex_launchpad.interfaces import IApexLaunchpad
from apex_launchpad.interfaces import ApexLaunchpadImplementation
from apex_launchpad.views import landing
from apex_launchpad.views import thanks

def includeme(config):
    settings = config.registry.settings

    config.registry.registerUtility(ApexLaunchpadImplementation, IApexLaunchpad)

    if not config.registry.queryUtility(IApex):
        raise MessageException('Apex isn\'t setup')
    
    config.add_subscriber('apex_launchpad.lib.subscribers.add_renderer_globals', 'pyramid.events.BeforeRender')

    config.add_static_view('apex_launchpad/static', 'apex_launchpad:static')

    if not settings.get('mako.directories'):
        config.add_settings({'mako.directories': ['apex_launchpad:templates']})

    render_template = getattr(settings, 'launchpad.launchpad_template', 'apex_launchpad:templates/launchpad_template.mako')

    config.add_route('apex_launchpad_landing', '/')
    config.add_view(landing, route_name='apex_launchpad_landing', renderer=render_template)

    config.add_route('apex_launchpad_thanks', '/thanks')
    config.add_view(thanks, route_name='apex_launchpad_thanks', renderer=render_template)    

    config.add_route('apex_launchpad_refer', '/r/:refer_id')
    config.add_view(landing, route_name='apex_launchpad_refer', renderer=render_template)

