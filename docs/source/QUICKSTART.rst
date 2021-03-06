Initial Setup of Apex Launchpad
===============================

::

    virtualenv --no-site-packages newenv
    cd newenv
    source bin/activate
    easy_install https://github.com/qwait/apex_launchpad/tarball/master
    paster create -t pyramid_routesalchemy example
    cd example
    vi development.ini

Changes made to **development.ini**

In the [app:example] section, add:

::

    apex.session_secret = CHANGEME
    apex.auth_secret = CHANGEME
    apex.came_from_route = home
    apex.velruse_config = %(here)s/CONFIG.yaml
    apex.recaptcha_public_key = xxxxxxxxxxxxxxxxxx
    apex.recaptcha_private_key = xxxxxxxxxxxxxxxxxx

If you do not include the recaptcha public and private key, the
login/registration forms will not include the ReCaptcha.net form.

If you need to get a key for ReCaptcha.net, go to:
https://www.google.com/recaptcha/admin/create and 'Create Key'

For Velruse, we need to add the following:

::

    [app:velruse]
    use = egg:velruse
    config_file = %(here)s/CONFIG.yaml
    beaker.session.data_dir = %(here)s/data/sdata
    beaker.session.lock_dir = %(here)s/data/slock
    beaker.session.key = velruse
    beaker.session.secret = somesecret
    beaker.session.type = cookie
    beaker.session.validate_key = STRONG_KEY_HERE
    beaker.session.cookie_domain = .domain.com

Comment or remove the following settings:

::

    [pipeline:main]
    pipeline =
        egg:WebError#evalerror
        tm
        example

Add the following settings:

::

    [filter:exc]
    use=egg:WebError#evalerror

    [pipeline:pexample]
    pipeline = exc tm example

    [composite:main]
    use = egg:Paste#urlmap
    / = pexample
    /velruse = velruse

If you are going to be developing with this virtualenv:

::

    python setup.py develop

Create your **CONFIG.yaml** file for Velruse. Currently, we need to access the
backing store, so, we've opted to use Type: SQL. You can use any store as
long as the backend can be read without calling /velruse/authinfo. The
Memory Store requires the additional urllib2 call.

::

    Store:
        Type: SQL
        DB: mysql://username:password@localhost/database?use_unicode=1&charset=utf8
    OpenID:
        Realm: http://domain.com
        Endpoint Regex: http://domain.com
    OpenID Store:
        Type: openid.store.memstore:MemoryStore

In **example/__init__.py**, before the return config.make_wsgi_app(), put:

::

    config.include('apex')
    config.include('apex_launchpad')

remove the route for '/'

The URLs created are / and /thanks

In **project/models.py**

::

    from apex_launchpad.models import ForeignKeyProfile
