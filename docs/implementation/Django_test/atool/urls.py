from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('universall/', views.new_universall, name="universall"),
    path('finance/', views.new_finance, name="finance"),
    path('election_report/', views.new_position, name="election_report"),
    path('advisory_member/', views.new_advisory, name="advisory_member"),
    path('intern/', views.get_all_by_electioninput, name="intern"),

    path('show/universal', views.change_universall, name="change_uni"),
    path('show/advisory', views.change_advisory, name="change_advi"),
    path('show/position', views.change_position, name="change_posi"),
    path('show/finance', views.change_finance, name="change_fin"),

]
