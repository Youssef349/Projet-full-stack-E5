from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant API",
        default_version="v1",
        description="Restaurant API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@restaurant.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register(r"orders", views.OrderViewSet)
router.register(r"reservations", views.ReservationViewSet)
router.register(r"menus", views.MenuViewSet)
router.register(r"menu-items", views.MenuItemViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("accounts/", include("rest_registration.api.urls")),
    re_path(
        r"^docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
