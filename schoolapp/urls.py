from django.urls import path
from schoolapp import views
urlpatterns = [
    path('school/',views.home),
    path('dashboard/',views.dashboard),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]
