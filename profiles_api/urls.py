from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()  # To create instance of DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')  # register router
router.register('profile', views.UserProfileViewSet)
router.register('demo', views.Demo)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name="hello"),
    path('', include(router.urls))  # Here we put blank url because we put base url hello-viewset
]


# urlpatterns = [
#     path('hello-view/', views.HelloApiView.as_view(), name="hello"),
#     path('hello-viewset/', views.HelloViewSet.as_view({'get':'list', 'put':'update'}))
# Here we can not put 2 time same methods in as_view({'get':'list','get':'create'}) perameter
# so that resister url as above
# ]
