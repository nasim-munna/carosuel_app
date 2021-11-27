from django.urls import path
from . import views
app_name = 'nasimit'
urlpatterns = [
    path('',views.index,name='name'),
    path('itsolution/',views.itsolution,name='itsolution'),
    path('contact_form/', views.contact, name='contact_form'),
    path('blog/', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    

]