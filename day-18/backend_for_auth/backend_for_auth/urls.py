
from django.contrib import admin
from django.urls import path,include
from user.swagger import schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('', include('secured_app.urls')),
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)