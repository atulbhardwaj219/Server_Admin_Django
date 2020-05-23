
from django.contrib import admin
from galaxy import  views
from django.conf.urls import url



urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$',views.home1, name='home1'),
    url(r'^createinstance/$',views.CreateInstance),
    url(r'^showinstance/$',views.ShowInstances),
    url(r'^startstop/$',views.StartStop),
    url(r'^requesthistory/$',views.RequestHistory),

]
