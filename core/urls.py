from django.urls import path, re_path # type: ignore
from .views import user_info, product_info

urlpatterns = [
    path("user/<int:user_id>/<str:username>", user_info, name="user"),
    re_path(
        r"^(?P<product_id>\d+)/(?P<product_name>\D+)", product_info, name="product"
    ),
]