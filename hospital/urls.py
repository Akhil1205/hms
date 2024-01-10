from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import hospitalListAPIView,hospitalUpdateAPIView,hospitalCreateAPIView

# router = DefaultRouter()
# router.register(r'hospitals', hospitalUpdateApi)

urlpatterns = [
    path('',hospitalListAPIView.as_view(),name='hospital_list' ),
    path('<int:id>/update/',hospitalUpdateAPIView.as_view()),
    path('create/',hospitalCreateAPIView.as_view())
]