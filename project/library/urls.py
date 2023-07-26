from django.urls import path
from library import views

urlpatterns = [
    path('<int:pk>', views.book_infos, name="infos")
]
