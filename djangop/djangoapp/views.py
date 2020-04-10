from django.shortcuts import render,redirect
from django.http import HttpResponse
from djangoapp.models import Student
from djangoapp.form import StudentForm,TestForm, CustomerForm
import csv
from reportlab.pdfgen import canvas
from django.core.mail import send_mail
from djangop import settings
from djangoapp.form import  UserForm, RegForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from djangoapp.functions import handle_uploaded_file
# Create your views here.
def index(request):
    return HttpResponse("Welcome to django!")

def show(request):
    return render(request,"test.html")

def display(request):
    name="Saurav Kumar"
    return render(request,'disp.html',{"uname":name})

def sample(request):
    name="Saurav Kumar"
    dept="CSE"
    return render(request,'sample.html',{'name':name, 'dept':dept})

def createStudent(request):
    students = Student.objects.all()
    return render(request,"students.html",{'students':students})

def createStudent1(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/createstudent")
    else:
        form=StudentForm()
        return render(request,'createstudent1.html',{'form':form})

def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("/createstudent")

def edit(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("/createstudent")
    else:
        form=StudentForm()
        return render(request,'editstudent.html',{'student':student})

def getcsv(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment;filename="student.csv"'
    writer=csv.writer(response)
    writer.writerow(['Id','Name','Marks'])
    writer.writerow(['100','Priya','90'])
    writer.writerow(['101','Puja','92'])
    return response

def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment;filename="sample.pdf"'
    c=canvas.Canvas(response)
    c.setFont("Times-Roman",42)
    c.drawString(100,700,"Hello Saurav Kumar !")
    c.showPage()
    c.save
    return response

def setsession(request):
    if request.method=='POST':

        form=TestForm(request.POST)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            request.session['name']=name #stores name in session
            request.session['email']=email #stores email in session
            return redirect('/getsession')
    else:
        form=TestForm()
    return render(request,'sess.html',{'form':form})


def getsession(request):
    name=request.session['name'] #fetches session vslue
    email=request.session['email'] #fetches session vslue
    return render(request,'result.html',{'name':name, 'email':email})

def setcookie(request):
    response=HttpResponse("Cookie Set!")
    response.set_cookie("mycookie","abcd")
    #my cookie is the name of the cookie
    return response

def getcookie(request):
    cookievalue=request.COOKIES["mycookie"] #fatches cookie value
    return HttpResponse("Cookie value is "+cookievalue)

def sendmail(request):
    subject = "Greetings"
    msg="Congratulations for your Success!"
    to="saurav001books@rediffmail.com"
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER, [to])
    if(res==1):
        msg="Mail sent succesfully!"
    else:
        msg="Mail could not be sent!"
    return HttpResponse(msg)

def customreg(request):
    if request.method=="POST":
        user=UserForm(request.POST)
        form=RegForm(request.POST)
        if user.is_valid() and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            user.save()
            profile.save()
            return redirect("/login/")
    else:
        user=UserForm()
        form=RegForm()
    return render(request,"registration/customreg.html",{'form':form,'user':user})    
 
def check(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)#logs in the user
        return redirect("/home")
    else:
        return redirect("/login")


@login_required
def home(request):
    username=request.user.username
    return render(request,"home.html",{'username':username})

def logoutview(request):
    logout(request) #It logsout the current user
    return redirect("/login")

def sample1(request):
    return render(request,"index.html",{'title':'home'})

def about(request):
    return render(request,"about.html",{'title':'about'})

def uploader(request):
    if request.method=="POST":
        form=CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            for f in request.FILES.getlist('file'):
                handle_uploaded_file(f)
            return HttpResponse('File uploaded successfully!')    
    else:
        c=CustomerForm()
        return render(request,'customer.html',{'form':c})

def firstpage(request):
    return render(request,'firstpage.html')