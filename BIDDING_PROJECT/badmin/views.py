from django.shortcuts import render,redirect
from user.models import UserRegistration
# Create your views here.
def chech_admin(request):
    username=request.POST["a1"]
    password=request.POST["a2"]
    if username=='admin' and password=='admin':
        return render(request,'badmin_templates/admin_home.html')
    else:
        return render(request,"badmin_templates/admin_login.html",{"msg":"inalid user"})


def admin_home(request):
    return render(request,"badmin_templates/admin_home.html")


def pending_reg(request):
    qs=UserRegistration.objects.filter(U_status="pending")
    return render(request,"badmin_templates/pending_registration.html",{"data":qs})

def approve_page(request):
    qs = UserRegistration.objects.filter(U_status="approved")
    return render(request,"badmin_templates/approve_registration.html",{"data":qs})

def approve_reg(request):
    idno=request.POST.get('a1')
    print(idno)
    qs=UserRegistration.objects.filter(U_idno=idno)
    print(qs)
    name=""
    cno=""
    for x in qs:
        name=x.U_name
        cno=x.U_contact
    qs.update(U_status="approved")
    # mess="hello mr/miss "+name+". Your registration is APPROVED"
    return pending_reg(request)



def decline_reg(request):
    idno=request.POST['a2']
    qs=UserRegistration.objects.filter(U_idno=idno)
    name=''
    cno=''
    for x in qs:
        name=x.U_name
        cno=x.U_contact
    qs.update(U_status="decline")
    return pending_reg(request)


def admin_contact(request):
    return render(request,"badmin_templates/admin_contact.html")


def admin_logout(request):
    return render(request,"badmin_templates/admin_login.html")


def decline_page(request):
    qs=UserRegistration.objects.filter(U_status="decline")
    return render(request,"badmin_templates/decline_registration.html",{"data":qs})