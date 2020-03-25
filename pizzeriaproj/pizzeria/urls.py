from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('gettypes/', views.gettypes, name='types'),
    path('getpizzas/', views.getpizzas, name='pizzas'),
    path('pizzadetails/<int:id>', views.pizzadetails, name='pizzadetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
