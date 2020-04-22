from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import core.urls
import user.urls

MEDIA_FILE_PATHS = static(
	settings.MEDIA_URL,
	document_root = settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(
        user.urls, namespace='user')),
    path('', include(
        core.urls, namespace='core')),
    
] + MEDIA_FILE_PATHS

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),

	] + urlpatterns

