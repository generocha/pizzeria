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
    path('newPizza/', views.newPizza, name='newpizza'),
    path('newPizzaType/', views.newPizzaType, name='newpizzatype'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
