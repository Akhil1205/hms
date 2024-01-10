from django.shortcuts import render
from rest_framework import generics
from .serializers import patientSerializer
# Create your views here.
from .models import patient,visited_time

class patientListAPIView(generics.ListAPIView):
    queryset=patient.objects.all()
    serializer_class=patientSerializer
class patientUpdateListAPIView(generics.RetrieveUpdateAPIView):
    queryset=patient.objects.all()
    serializer_class=patientSerializer
    lookup_field='id'
    def perform_update(self,serializer):
        serializer.save()