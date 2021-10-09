from django.urls import path
from . import views
app_name = 'carosuel'
urlpatterns = [
    path('carosuel/',views.index,name='name'),
]