from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('universall/', views.new_universall, name="universall"),
    path('finance/', views.finance, name="finance"),
    path('election_report/', views.election, name="election_report"),
    path('advisory_member/', views.advisory, name="advisory_member"),
    path('intern/', views.intern, name="intern"),
]
