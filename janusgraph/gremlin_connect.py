from django.views import View

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

class BaseGremlinClass(View):
    def __init__(self):
        self.g = traversal().withRemote(DriverRemoteConnection('ws://192.168.99.100:8182/gremlin','g'))
        pass
