from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:article_id>/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('redact/<int:article_id>/', views.redact, name='redact'),
    path('redact/send', views.update_article, name='send'),
]