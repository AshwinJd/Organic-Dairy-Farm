
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from cattle import views as cattle_views


urlpatterns = [
   	url(r'^$', include("cattle.urls")),
   	#url(r'^home/', cattle_views.home),
 	url(r'^admin/', admin.site.urls),
 	url(r'^cattlepage/',include('cattle.urls')),
 	url(r'^calfpage/',include('calf.urls')),	
 	url(r'^custpage/',include('customer.urls')),
 	url(r'^invoicepage/',include('invoice.urls')),
 	url(r'^accounts/', include('registration.backends.default.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)