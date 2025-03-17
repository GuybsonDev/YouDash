# ifood_dashboard/urls.py
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

@api.get('media/')
def livro(request):
    return 'Os dados serão inseridos aqui'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
