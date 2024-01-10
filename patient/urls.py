from django.urls import path
from .views import patientListAPIView,patientUpdateListAPIView
urlpatterns = [
    path('',patientListAPIView.as_view(),name='patient_list' )
    ,path('<int:id>/update/',patientUpdateListAPIView.as_view())
   
]