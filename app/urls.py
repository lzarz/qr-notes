from django.urls import path
from . import views

urlpatterns = [
	path("", views.landing_page, name="landing_page"),
        path('guide/', views.how_to_use, name='how_to_use'),
        path('create/', views.create_note, name='create_note'),
        path('view/<str:token>/', views.view_note, name='view_note'),
        path('about/', views.about, name='about'),
]
