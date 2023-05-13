from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import random
from .models import *
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail
from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from cryptography.fernet import Fernet
import base64
from django.contrib.auth.decorators import login_required

User = get_user_model()
def home(request):
    if request.method=='POST':
        email=request.POST.get('useremail')
        password=request.POST.get('password')

        user=authenticate(request,email=email,password=password)
        if user is None:
            return render(request,'homepage/home.html')
        auth.login(request,user)
        if user.is_superuser:
            return redirect('/admin_panel/')
        elif user.is_staff:
            return redirect('/dep_deshboard/')
        elif user:
            return redirect('/stdprofile/')
        else:
            return render(request,'homepage/home.html')
    return render(request,'homepage/home.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if password == cpassword:
            User = get_user_model()
            user=User.objects.create_user(email=email,password=password)
            user.save()
            return redirect('/')  
    return render(request,'homepage/signup.html')     

def forgotusername(request):
    if request.method != 'POST':
        return render(request,'homepage/forgotusername.html' )
    User = get_user_model()
    useremail=request.POST.get('useremail')
    useremail2=User.objects.get(email= useremail)

    if useremail2 is None:
        return render(request,'homepage/forgotusername.html' )
    otp=random.randint(1,10000)
    request.session['otp']=otp
    request.session['email']=useremail

    subject = 'OTP for reset password'
    message = """otp :%d
                      """ %otp
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [useremail2, ]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/forgototp/')


def forgototp(request):
    if request.method=='POST':
        otp=int(request.POST.get('otp'))

        if (otp==int(request.session.get('otp'))):
            return redirect('/forgotpassword/')  
        else:
            return render(request,'homepage/forgototp.html' )
    return render(request,'homepage/forgototp.html' )

def forgotpassword(request):
    if request.method != 'POST':
        return render(request,'homepage/forgotpassword.html' )
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    if password != cpassword:
        return render(request,'homepage/forgotpassword.html' )
    User = get_user_model()
    user=User.objects.get(email=request.session.get('email'))
    user.set_password(password)
    user.save()
    return redirect('/')

@login_required
def stdprofile(request):
    useremail=request.user.email
    empdata=Userdetail.objects.filter(email=useremail)
    return render(request,'student/stdprofile.html',{'empdata':empdata})

@login_required
def stdleave(request):
    id=request.user.id

    if request.method=='POST':
        empname=request.POST.get('empname')
        depmnt=request.POST.get('depmnt')
        leavereq=request.POST.get('noofleave')
        leavepur=request.POST.get('leavepurpose')
        applydatefrom=request.POST.get('datefrom')
        applydateto=request.POST.get('dateto')
       
        create_leave=leaveinformation.objects.create(name=empname,department=depmnt,applyleave=leavereq,leavepurpose=leavepur,leavedatefrom=applydatefrom,leavedateto=applydateto)
        create_leave.save()

        return redirect('/stdprofile/')

    return render(request,'student/stdleave.html')

@login_required
def dep_deshboard(request):
    return render(request,'department/dep_deshboard.html')

@login_required
def allemployee(request):
    currentuser=request.user.department
    data=Userdetail.objects.filter(department=currentuser)
    return render(request,'department/allemp_dep.html',{'data2':data})

@login_required
def newemp(request):
    currentuser=request.user.department
    data=Userdetail.objects.filter(department=currentuser)
    return render(request,'department/newemp.html',{'data':data})

@login_required
def update(request,id):
    var=id
    userdata=Userdetail.objects.get(id=var)
    return render(request,'department/update.html',{'userdata':userdata,'idd':var})  

@login_required
def updatedetails(request,id):
    if request.method != 'POST':
        return render(request,'update.html')
    new_id = id
    empname=request.POST.get('empname')
    # email=request.POST.get('email')
    fname=request.POST.get('fname')
    mname=request.POST.get('mname')
    department=request.POST.get('department')
    empid=request.POST.get('empid')
    empdeg=request.POST.get('empdeg')
    empjoiningdate=request.POST.get('empjoiningdate')
    empleave=request.POST.get('empleave')
    empsalary=request.POST.get('empsalary')
    empcontact=request.POST.get('empcontact')
    empaddress=request.POST.get('empaddress')
    emppic=request.FILES.get('emppic')

    Userdetail.objects.filter(new_id=new_id).update(
        employeename=empname,
        fathername=fname,
        mothername=mname,
        department=department,
        employeeid=empid,
        employeedegination=empdeg,
        joiningdate=empjoiningdate,
        employeeleave=empleave,
        employeesalary=empsalary,
        employeecontect=empcontact,
        employeeaddress=empaddress,
        employeepic=emppic,
    )
    return redirect('/newemp')

@login_required
def Delete1(request,id):
    data1=Userdetail.objects.filter(id=id)
    data1.delete()
    return redirect('/allemployee/')

@login_required
def empleave(request):
    currentuser=request.user.department
    leavedetail=Userdetail.objects.filter(department=currentuser)
    return render(request,'department/employeeleave.html',{'leavedetail':leavedetail})

@login_required
def empsalary(request):
    currentuser=request.user.department
    salarydetail=Userdetail.objects.filter(department=currentuser)
    return render(request,'department/employeesalary.html',{'salarydetail':salarydetail})

@login_required
def leaveapproval(request):
    userdepartment=request.user.department
    data=leaveinformation.objects.filter(department=userdepartment,leavestatus='pending')
    return render(request,'department/leave_approval.html',{'data':data})

@login_required
def rejectleave(request,id):
    data=leaveinformation.objects.filter(id=id)
    data.delete()
    return render(request,'department/leave_approval.html/')

@login_required
def approved1(request,id):
    leaveinformation.objects.filter(id=id).update(leavestatus='Approved')
    empname=leaveinformation.objects.filter(id=id)
    e=leaveinformation.objects.get(id=id)

    for i in empname:
       name=i.name
       aleave=int(i.applyleave)
       tleave=Userdetail.objects.filter(username=name)
       for i in tleave:
           total_leave=int(i.employeeleave)
           leave=total_leave-aleave
           Userdetail.objects.filter(username=name).update(employeeleave=leave)
           return redirect('/dep_deshboard/')
    return render(request,'department/leave_approval.html')

@login_required
def admin_panel(request):
    return render(request,'admin/admin_panel.html')

@login_required
def create_account(request):
    if request.method != 'POST':
        return render(request,'admin/create_account.html')
    username=request.POST.get('username')
    email=request.POST.get('email')
    department1=request.POST.get('department')
    degination=request.POST.get('degination')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')

    if password == cpassword:
        User = get_user_model()
        user=User.objects.create_user(
        email=email,password=password,username=username,department=department1,employeedegination=degination)
        user.save()
    if degination in ['Manager', 'HOD']:
        Userdetail.objects.filter(employeedegination=degination).update(is_staff=1,is_active=1)
    Userdetail.objects.filter(employeedegination=degination).update(is_active=1)
    return redirect('/admin_panel/')

@login_required
def allemployee2(request):
    userdep=request.user.department
    data=Userdetail.objects.all().exclude(department=userdep)
    return render(request,'admin/allemployee2.html',{'data':data})

@login_required
def alldepartment(request):
    if request.method=='POST':
        dep=request.POST.get('department')
        data=Userdetail.objects.filter(department=dep)
        return render(request,'admin/alldepartment.html',{'data':data})
    return render(request,'admin/alldepartment.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def Delete(request,id):
    data1=Userdetail.objects.filter(id=id)
    data1.delete()
    return redirect('/allemployee2/')

@login_required
def leave(request):
    userdep=request.user.department
    leavedata=Userdetail.objects.all().exclude(department=userdep)
    return render(request,'admin/leave.html',{'leavedata':leavedata})

@login_required
def salary(request):
    userdep=request.user.department
    salarydata=Userdetail.objects.all().exclude(department=userdep)
    return render(request,'admin/salary.html',{'salarydata':salarydata})
