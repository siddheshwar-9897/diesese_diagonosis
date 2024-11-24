from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.forms import RegisterForm
from .models import Member
from .forms import MemberForm


# Create your views here.
def index(request):
    
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def form(request):
    return render(request,'form.html')

def chatbot(request):
    return render(request,'chatbot.html')

def dietplan(request):
    return render(request,'dietplan.html')

def terms(request):
    return render(request,'terms.html')

def question(request):
    return render(request,'question.html')

# def prediction(request):
#     return render(request,'prediction.html')

def prediction(request):
    if request.method=='POST':
        # Age=request.POST['Age']
        BloodPressure=request.POST['BloodPressure']
        SpecificGravity=request.POST['SpecificGravity']
        Albumin=request.POST['Albumin']
        Sugar=request.POST['Sugar']
        BloodGlucoseRandom=request.POST['BloodGlucoseRandom']
        BloodUrea=request.POST['BloodUrea']
        SerumCreatinine=request.POST['SerumCreatinine']
        Sodium=request.POST['Sodium']
        Potassium=request.POST['Potassium']
        Hemoglobin=request.POST['Hemoglobin']
        PackedCellVolume=request.POST['PackedCellVolume'] 
        WhiteBloodCell=request.POST['WhiteBloodCell']
        RedBloodCell=request.POST['RedBloodCell']
        # print(
        #       type(BloodPressure),
        #       type(SpecificGravity),
        #       type(Albumin),
        #       type(Sugar),
        #       type(Sodium),
        #       type(BloodGlucoseRandom),
        #       type(BloodUrea),
        #       type(SerumCreatinine),
        #       type(Potassium),
        #       type(Hemoglobin),
        #       type(PackedCellVolume),
        #       type(WhiteBloodCell),
        #       type(RedBloodCell)
        #       )

        lis=[BloodPressure,SpecificGravity,Albumin,Sugar,BloodGlucoseRandom,BloodUrea,SerumCreatinine,Sodium,Potassium,Hemoglobin,PackedCellVolume,WhiteBloodCell,RedBloodCell]
        print(lis)

            #training mode
        from joblib import load
        model=load('C:\\Users\\91932\\OneDrive\\Desktop\\d jango\\kideny\\model.joblinb')


        #make prediction
        result = model.predict([lis[:11]])  # Select the first 11 features and reshape to 2D

        print(result)

        if result[0]==0:
            print('no')
            value='Negative'

        else:
            print("yes")
            value='Postive'

    return render(request,'prediction.html',{
        'ans':value,
        'title':'predict'

    })
        

        #addd
def add(request):
    if request.method=='POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=MemberForm()
    return render(request,'add.html',{'form':form})

#-------------------------------------------------------
def home(request):
    mem=Member.objects.all()
    return render(request,'home.html',{'mem':mem})

#----------------------------------------

def update(request,id):
    mem= get_object_or_404(Member,id=id)
    if request.method=='POST':
        form=MemberForm(request.POST,instance=mem)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=MemberForm(instance=mem)
    return render(request,'update.html',{'form':form})

def delete(request,id):
     mem= get_object_or_404(Member,id=id)
     mem.delete()
     return redirect('home')

def filter_details(request):
    mem=Member.objects.all()


    #filtering logic
    firstname_query= request.GET.get('firstname')
    lastname_query= request.GET.get('lastname')
    country_query= request.GET.get('countryname')


    return render(request,'filter_details.html',{'mem':mem})


def register(request):

    

    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('login_view')
    else:
         form= RegisterForm()
    return render(request,'register.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('form')
    else:
        form =AuthenticationForm()
    return render(request,'login.html',{'form':form})  

