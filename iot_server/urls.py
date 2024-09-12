from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # swagger-ui
    path(
        "api-schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # App URLs
    path("automation/", include("automation.urls")),
]
