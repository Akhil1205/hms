from django.shortcuts import render,redirect,get_object_or_404
from .models import hospital
from rest_framework import generics,viewsets
from .serializers import hospitalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import hospitalForm

# Create your views here.
def hospital_list(request,*args,**kwargs):
    hospitals = hospital.objects.all()
    return render(request, 'hospital/list.html', {'hospitals': hospitals})
# class hospitalListView(generics.ListAPIView):
#     queryset = hospital.objects.all()
#     serializer_class = hospitalSerializer
def hospital_detail_view(request,id):
    instance = get_object_or_404(hospital, id=id)
    return render(request, 'hospital/detail.html', {'instance': instance})
def add_hospital(request):
    if request.method == 'POST':
        form = hospitalForm(request.POST)
        if form.is_valid():
            form.save()
            form = hospitalForm()
           # Redirect to the list view after successful creation
    else:
        form = hospitalForm()

    return render(request, 'hospital/create.html', {'form': form})
def update_hospital(request, id):
    instance = get_object_or_404(hospital, id=id)

    if request.method == 'POST':
        form = hospitalForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            form = hospitalForm()
            # return redirect('hospital-list')  # Redirect to the list view after successful update
    else:
        form = hospitalForm(instance=instance)

    return render(request, 'hospital/update.html', {'form': form, 'id': id})
class hospitalListAPIView(generics.ListAPIView):
    queryset = hospital.objects.all()
    serializer_class = hospitalSerializer
class hospitalUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = hospital.objects.all()
    serializer_class = hospitalSerializer
    lookup_field='id'
    def perform_update(self, serializer):
        # Update hospital details
        instance = serializer.save()
        # Update associated departments if 'department' data is included in the request
        department_ids = self.request.data.get('department', [])
        if department_ids:
            instance.department.set(department_ids)


class hospitalCreateAPIView(generics.CreateAPIView):
    queryset = hospital.objects.all()
    serializer_class = hospitalSerializer

    def perform_create(self, serializer):
        serializer.save()

