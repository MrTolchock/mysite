from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("personal.urls")),
    url(r'^delay/', include("delay.urls")),
    url(r'^fitness/', include("fitness.urls")),
    url(r'^favicon.ico$',
        RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'),),
        name="favicon"),    
]
