from zope.interface import implements
from zope.interface import Interface

class IPyramidLaunchpad(Interface):
    pass
    
class PyramidLaunchpadImplementation(object):
    implements(IPyramidLaunchpad)