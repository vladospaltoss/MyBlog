from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
    path('form/', views.form_page, name='form page'),
    path('thanks/', views.thanks_page, name='thanks'),
]