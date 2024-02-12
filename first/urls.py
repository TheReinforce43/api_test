from django.urls import path 
from . import views 

urlpatterns = [
    path('teacher/',views.teacher_info,name='teacher_info'),
    path('teacher/<int:pk>',views.teacher_instance,name='teacher_instance'),
    path('teacher_create/',views.teacher_create,name='teacer_create'),
    path('teacher_api/',views.teacher_apiView,name='teacer_api'),
    path('teacher_api/<int:pk>',views.teacher_apiView,name='teacer_api'),
]
