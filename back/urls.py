from django.urls import path
from . import views


urlpatterns = [
    path('', views.Tareas.as_view(), name='home'),
    path('nuevo/', views.Nuevo.as_view(), name='nuevo'),
    path('<int:pk>/', views.Ver.as_view(), name='ver'),
    path('<int:pk>/borrar/', views.Borrar.as_view(), name='borrar'),
]
