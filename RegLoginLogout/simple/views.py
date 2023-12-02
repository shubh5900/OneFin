from django.shortcuts import render,redirect

from simple.models import Reg
# Create your views here.

def Registration(request):
    if request.method=="POST":
        name = request.POST['Name']
        Father = request.POST['Father']
        Mother = request.POST['Mother']
        Age = request.POST['Age']
        Gender=request.POST['Gender']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Reg(Name=name,FatherName=Father, MotherName=Mother, Age=Age,Gender=Gender, Email=Email, Password=Password).save()
        
        Successful="Registration complete successful! please Login"
        print(Reg.objects.all())

        return render(request,"Login.html", {"Success":Successful})


    return render(request,"Registration.html")

def Login(request):
    if request.method=="POST":
        Email=request.POST["Email"]
        Password=request.POST["Password"]
        user=Reg.objects.filter(Email=Email)
        print(user)
        #print(user.filter(Password==Password))
        if user.filter(Password=Password):
            return redirect("/Home/")
        else:
            message="Email or Password if wrong!"
            return render(request,"Login.html", {"message":message})
    
    return render(request,"Login.html")

def Home(request):
   return render(request,"Home.html")
    
    

