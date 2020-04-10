from django.urls import path
from .views import UserList, GetToken
#from rest_framework.authtoken.views import obtain_auth_token

app_name = "user"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('user/', UserList.as_view()),
    path('authtoken/', GetToken.as_view())
]
