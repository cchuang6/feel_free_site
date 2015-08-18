from django.db import models
from parse_rest.connection import register
from parse_rest.datatypes import GeoPoint, Object
from parse_rest.user import User
from django.conf import settings

# Create your models here.

# Register connection for Parse.com here
register(
    getattr(settings, 'APPLICATION_ID', ''),
    getattr(settings, 'REST_API_KEY', ''),
    master_key=getattr(settings, 'MASTER_KEY', '')
)

class City(Object):
    pass

class BriefConnectedFriends(Object):
    pass

class ConnectedFriends(Object):
    pass

class Connections(Object):
    pass

class History(Object):
    pass

class Messages(Object):
    pass

class Nods(Object):
    pass

class Space(Object):
    pass



