from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.artistList,name="artist"),
    path('detail/<str:pk>/', views.artistdetail, name="detail"),
    path('create/',views.artistCreate,name="create"),
    path('update/<str:pk>/',views.artistUpdate,name="update"),
    path('delete/<str:pk>/',views.artistDelete,name="delete"),
    ]


