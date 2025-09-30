from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def chrome_devtools_json(request):
    return HttpResponse(status=204)

urlpatterns = [
    path('', home, name='home'),
    path('.well-known/appspecific/com.chrome.devtools.json', chrome_devtools_json)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)