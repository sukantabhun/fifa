from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("",views.index,name='home'),
    path("MatchScore",views.MatchScore,name='MatchScore'),
    path("DashBoard",views.DashBoard,name='DashBoard'),  
    path("Custom",views.Custom,name='Custom'),
    path("LiveMatch",views.LiveMatch,name='LiveMatch')   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
