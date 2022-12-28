from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('loginview', views.loginview, name='loginview'),
    path('login/process', views.process, name='process'),
    path('logout', views.processlogout, name='processlogout'),
    path('signup2', views.signup2, name='signup2'),
    path('signup', views.signup, name='signup'),
    path('choose', views.choose, name='choose'),
    path('home', views.home, name="home"),
    path('processadd', views.processadd, name = 'processadd'),
    path('<int:profiletab>/detail/', views.detail, name = 'detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.
STATIC_URL, document_root = settings.STATIC_ROOT)