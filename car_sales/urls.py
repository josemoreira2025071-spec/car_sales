from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Define urlpatterns PRIMEIRO
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),
]

# Depois adiciona as rotas de media (só em desenvolvimento)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)