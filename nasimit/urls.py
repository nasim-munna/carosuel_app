from django.urls import path
from . import views
app_name = 'nasimit'
urlpatterns = [
    path('',views.index,name='name'),
]