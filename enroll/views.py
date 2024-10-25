from django.shortcuts import render, HttpResponseRedirect
from .forms import studentRegistration
from .models import User
# Create your views here.


def add_and_show(request):
    if request.method == "POST":
        frm = studentRegistration(request.POST)

        if frm.is_valid():
            frm.save()

        frm = studentRegistration()
    else:
        frm = studentRegistration()

    data = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': frm, 'data': data})


def update_data(request, id):
    user = User.objects.get(pk=id)

    if request.method == "POST":
        frm = studentRegistration(request.POST, instance=user)

        if frm.is_valid():
            frm.save()

    else:
        frm = studentRegistration(instance=user)

    return render(request, 'enroll/updatestudent.html', {'form': frm, 'id': id})


def delete_data(request, id):

    user = User.objects.get(pk=id)
    user.delete()

    return HttpResponseRedirect('/')
