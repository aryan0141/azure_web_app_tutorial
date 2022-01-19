from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('openapi/', get_schema_view(
        title="API Documentation",
        description="API for all things",
        version="1.0.0"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger_doc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger_doc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
