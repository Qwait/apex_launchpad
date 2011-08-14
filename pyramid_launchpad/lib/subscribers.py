from pyramid.threadlocal import get_current_request

from pyramid_launchpad.lib.launch import launch_settings

def add_renderer_globals(event):
    request = event.get('request')
    if request is None:
        request = get_current_request()

    globs = {
        'launch_settings': launch_settings,
    }
    event.update(globs)