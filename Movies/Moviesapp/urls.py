from . import views
from django.urls import path
app_name= 'Moviesapp'

urlpatterns = [
    path('',views.movies,name='movies'),
    path('movie/<int:movies_id>/', views.detail,name='detail'),
    path('add/',views.add_movie,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]