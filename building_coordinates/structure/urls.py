from django.urls import path
from . import views


app_name = 'structure'

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('create/', views.structure_create, name='create'),
    path('api/v1/get_all_adress/', views.StructureAllViewAPI.as_view()),
    path('api/v1/<str:address>/', views.StructureAdressViewAPI.as_view()),
]
