from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('universall/', views.new_universall, name="universall"),
    path('finance/', views.new_finance, name="finance"),
    path('election_report/', views.new_position, name="election_report"),
    path('advisory_member/', views.new_advisory, name="advisory_member"),
    path('conduct/', views.new_conduct, name="conduct"),
    path('intern/', views.get_all_by_electioninput, name="intern"),

    path('show/universall/', views.change_universall, name="change_uni"),
    path('show/advisory/', views.change_advisory, name="change_advi"),
    path('show/position/', views.change_position, name="change_posi"),
    path('show/finance/', views.change_finance, name="change_fin"),
    path('show/conduct/', views.change_conduct, name="change_con"),

    path('', include('django.contrib.auth.urls')),
]
