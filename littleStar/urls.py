from django.conf.urls import url
from littleStar import views
from django.conf.urls.static import static
from django.conf import settings

# SET THE NAMESPACE!
app_name = 'littleStar'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^/$',views.index,name='index'),
    url(r'^index/$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^kidDetailsRedirect/$',views.detailRedirect,name='kidDetails'),
    url(r'^createSchool/$',views.createSchool,name='createSchool'),
    url(r'^anthropometry/$', views.anthropometryView, name = 'anthropometry'),
    url(r'^dental/$', views.dental, name = 'dental'),
    url(r'^pediatrics/$', views.pediatrics, name = 'pediatrics')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)