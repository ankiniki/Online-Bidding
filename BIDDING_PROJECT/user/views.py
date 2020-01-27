
from django.shortcuts import render, redirect
from .models import UserRegistration
from user.models import ProductModel
# Create your views here.
def user_home(request):
    return render(request,"user/user_home.html")



def userlogin(request):
    contact=request.POST.get("b1")
    password=request.POST.get("b2")
    try:
        res=UserRegistration.objects.get(U_contact=contact,U_password=password)
        if res.U_status == 'approved':
            request.session['user_username']=res.U_name
            request.session['user_idno']=res.U_idno
            request.session['user_usercontact']=res.U_contact
            return render(request,"user/user_home.html")
        elif res.U_status == 'pending':
            return render(request, "user/login_user.html",{"msg":"your request is pending"})
        else:
            return render(request, "user/login_user.html",{"msg":"your request is decline"})
    except UserRegistration.DoesNotExist:
        return render(request, "user/login_user.html",{"msg":"inalid user"})


def user_reg(request):
    name = request.POST["s1"]
    contact = request.POST["s2"]
    email = request.POST["s3"]
    password = request.POST["s4"]
    status = "pending"
    puser=request.session['user_useridno']
    UserRegistration(U_name=name,U_contact=contact,U_email=email,U_password=password,U_status=status,user_id=puser).save()
    return redirect("buyer_seller")


def bid_product(request):
    return render(request, "user/bid_product.html")


def logout_user(request):
    del request.session['user_username']
    return redirect('main')

def save_product(request):
    pid=request.POST["p1"]
    name=request.POST["p2"]
    bprice=request.POST["p3"]
    pinfo=request.POST["p4"]
    pimage=request.FILES["p5"]
    pstatus='bidding'
    puser=request.session['user_idno']
    ProductModel(pid=pid,name=name,bprice=bprice,info=pinfo,image=pimage,status=pstatus,user_id=puser).save()
    res=ProductModel.objects.all()
    return redirect('sell_product')


def sell_product(request):
    data=ProductModel.objects.filter(user_id=request.session['user_idno'])
    return render(request, "user/sell_product.html",{"data":data})