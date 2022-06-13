from django.urls import path
from computerApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machines', views.machine_list_view, name='machines'), 
    path('machine/<pk>', views.machine_detail_view, name='machine-detail'),  
    path('add-machine', views.machine_add_form, name='add-machine'),
    path('b.html', views.b , name='b.html'),
    path('d.html', views.d , name='d.html'),
    path('e.html', views.e , name='e.html'),
    path('contact.html', views.contact , name='contact.html'),
]   
