from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('first', views.FirstView)
router.register('second', views.SecondView)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls), name = 'api')
]
