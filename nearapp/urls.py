from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', views.filterList)
# router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.filterPage, name='index'),
    path('<int:pk>/<str:type>', views.typefilterPage, name='filtertype'),
    path('shop/<int:pk>', views.detailsPage, name='shop'),
    path('api/<int:pk>/', views.filterApi, name='api'),
    path('filter', views.filterApi, name='filter'),
    path('suggestions', views.suggestions, name='suggestions'),
    path('faqs', views.faq, name='faq'),
    path('about', views.aboutUs, name='about'),
    path('chatapi', views.chat, name='chat'),
    # path('getAllCol', views.getAllCollegs, name='getAllCol'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
