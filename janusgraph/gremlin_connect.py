from django.views import View
from django.conf import settings

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

class BaseGremlinClass(View):
    def __init__(self):
        self.g = traversal().withRemote(DriverRemoteConnection(settings.GREMLIN_HOST,'g'))
        pass
