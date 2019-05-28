from django.shortcuts import render
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import NodeForm, RelationshipForm

# Create your views here.
class SimpleGremlinView(View):
    def __init__(self):
        self.__g = traversal().withRemote(DriverRemoteConnection('ws://192.168.99.100:8182/gremlin', 'g'))
        pass

    def get(self, request):
        all_nodes = [
                {'entityName' : p }
                for p in self.__g.V().hasLabel('person').values('entityName').toList()
                ]
        return JsonResponse({"nodes" : all_nodes})

class NodeFormClass(View):
    def get(self, request):
        return render(request, 'nodeform.html', {'form' : NodeForm()})

    def post(self, request):
        form = NodeForm(request.POST)
        if form.is_valid():
            g = traversal().withRemote(DriverRemoteConnection('ws://192.168.99.100:8182/gremlin','g'))
            g.addV('person').property('entityName', form.cleaned_data['entityName']).property('first_name', form.cleaned_data['first_name']).property('last_name', form.cleaned_data['last_name']).next()
            resp = { "action" : "create", "node" : { "entityName" : form.cleaned_data['entityName'], "first_name" : form.cleaned_data['first_name'], "last_name" : form.cleaned_data['last_name'] }}
            return JsonResponse(resp)

class RelationshipFormClass(View):
    def __init__(self):
        self.__g = traversal().withRemote(DriverRemoteConnection('ws://192.168.99.100:8182/gremlin','g'))
        pass
    def get(self, request):
        return render(request, 'relationshipform.html', {'form' : RelationshipForm()})

    def post(self, request):
        form = RelationshipForm(request.POST)
        if form.is_valid():
            entityA = self.__g.V().hasLabel('person').has('entityName', form.cleaned_data['entityA']).next()
            entityB = self.__g.V().hasLabel('person').has('entityName', form.cleaned_data['entityB']).next()
            relationship = form.cleaned_data['relationship']
            self.__g.addE(relationship).from_(entityA).to(entityB).next()
            resp = {
                    "action" : "relationship_create",
                    "relationship" : {
                        "entityA" : form.cleaned_data['entityA'],
                        "relationship" : relationship,
                        "entityB" : form.cleaned_data['entityB']
                    }
            }
            return JsonResponse(resp)
