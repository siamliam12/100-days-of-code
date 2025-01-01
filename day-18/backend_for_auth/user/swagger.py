from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Authentication System",
        default_version='v1',
        description='''
        Different types of authentication
        For Authorizing use the value as {Bearer your_api_key}
        ''',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

