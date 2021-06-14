from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('universall/', views.new_universall, name="universall"),
    path('finance/', views.new_finance, name="finance"),
    path('election_report/', views.new_position, name="election_report"),
    path('advisory_member/', views.new_advisory, name="advisory_member"),
    path('intern/', views.get_universall, name="intern"),
]
