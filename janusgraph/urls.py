from django.urls import path
from . import views

urlpatterns = [
    path('all_nodes/', views.SimpleGremlinView.as_view()),
    path('create_node/', views.NodeFormClass.as_view()),
    path('create_relationship/', views.RelationshipFormClass.as_view()),
    path('node_information/', views.NodeInformation.as_view())
]
