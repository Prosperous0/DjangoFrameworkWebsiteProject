from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Main web pages (your existing landing page, etc.)
    path('', include('recipes.urls')),
    
    # REST API endpoints
    path('api/', include('recipes.api_urls')),
]
