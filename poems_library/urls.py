from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="poems_library/index.html"), name="index"
    ),
    path("poems/", views.PoemsListView.as_view(), name="poems_list"),
    path("poems/<int:pk>", views.PoemDetailView.as_view(), name="poem"),
    path("poems/create", views.PoemCreateView.as_view(), name="create_poem"),
    path("poems/<int:pk>/delete", views.PoemDeleteView.as_view(), name="delete_poem"),
    path("poems/<int:pk>/update", views.PoemUpdateView.as_view(), name="update_poem")
]
