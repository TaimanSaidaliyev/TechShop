from django.urls import path

from . import views

urlpatterns = [
    path(
        "product/<int:product_id>/",
        views.FeedbackView.get,
    ),
    path("product/<int:product_id>/add", views.FeedbackView.add),
]
