from django.contrib import admin
from django.urls import path
from awardsapp import views

urlpatterns=[
    path("", views.index, name="index"),
    path('profile/',views.profile,name = 'profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_picture, name='update_profile'),
    path('project/', views.upload_project, name = "upload"),
    path('search/', views.search, name='search'),
    path("project/<int:project_id>/", views.project_details, name="project_details"),
    path('rate/<int:id>', views.rating, name='rate'),
    
]

