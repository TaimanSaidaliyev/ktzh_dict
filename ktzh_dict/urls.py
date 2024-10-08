from django.contrib import admin
from django.urls import path
from employees.views import *
from django.conf import settings
from django.conf.urls.static import static
from employees.forms import DivisionAutocomplete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('division-autocomplete/', DivisionAutocomplete.as_view(), name='division-autocomplete'),
    path('employee/<int:id>/', employee_profile, name='profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
