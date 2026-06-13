from django.shortcuts import render,redirect,get_object_or_404
from .models import Hospital
from .forms import HospitalForm
from django.contrib import messages
from django.db.models import Q #to target the entered data.
from django.contrib.auth.decorators import login_required


# Create your views here.
#create
@login_required(login_url='signin')
def home(request): 
    form = HospitalForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Detaills created successfullyy!.....')
        return redirect('read_hospital')  
    return render(request,'home.html',{'form':form})   


#read-->extract the data display the data.
@login_required(login_url='signin')
def read_hospital(request):
    search = request.GET.get('q')#it will recive the data written in input tag of serach bar
    if search:
        data=Hospital.objects.filter(
            Q(name__icontains = search) |
            Q(disease__icontains = search) |
            Q(doctor_assigned__icontains = search) |
            Q(age__icontains = search) |
            Q(room_number__icontains = search) 
        )
    else:
      data = Hospital.objects.all()# to retrive the all data
    return render(request,'read_hospital.html',{'keerthana':data,'search':search})

#update -->extract the data update the data.
@login_required(login_url='signin')
def update_hospital(request, pk): #view
    data = get_object_or_404(Hospital, id=pk) #extract
    form = HospitalForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,'details updatted successfullyy!.....')
        return redirect('read_hospital')  
    return render(request,'update_hospital.html',{'form':form})
    
#delete --extract the data delete the data
@login_required(login_url='signin')
def delete_hospital(request,pk):
    data = get_object_or_404(Hospital, id=pk) 
    if request.method=='POST':
        data.delete()
        messages.success(request,'Details deleted successfullyy!.....')
        return redirect('read_hospital')
    return render(request,'delete_hospital.html')  