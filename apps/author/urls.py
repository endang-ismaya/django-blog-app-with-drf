from django.urls import path


from apps.author import views


urlpatterns = [
    path("", views.index, name="author.index"),
]
