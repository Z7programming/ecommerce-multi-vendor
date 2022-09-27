
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
print("_"*90)
urlpatterns = [
    # accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # apps
    path('', include('Home.urls', namespace='Home')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    # admin
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
