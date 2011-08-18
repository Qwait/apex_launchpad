from zope.interface import implements
from zope.interface import Interface

class IApexLaunchpad(Interface):
    pass
    
class ApexLaunchpadImplementation(object):
    implements(IApexLaunchpad)