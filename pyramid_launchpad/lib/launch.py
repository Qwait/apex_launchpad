from pyramid.threadlocal import get_current_registry

def launch_settings(key=None):
    settings = get_current_registry().settings

    if key:
        return settings.get('launchpad.%s' % key)
    else:
        launchpad_settings = []
        for k, v in settings.items():
            if k.startswith('launchpad.'):
                launchpad_settings.append({k.split('.')[1]: v})

        return launchpad_settings