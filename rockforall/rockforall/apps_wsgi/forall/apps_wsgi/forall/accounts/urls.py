from django.urls import path, include
# IMPORT DAS VIEWS
from . import views
# -------------------
urlpatterns = [
	path('register/',views.SignUp.as_view(), name="cadastra"),
]