from django.urls import path
from .views import FilesView
app_name = "storage"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('files/', FilesView.as_view()),
]
