from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def dashboard(request):
    try:
        
        u1=SocietyMembers.objects.get(Email=request.session['email'])
        return render(request,'dashboard.html',{'userdata':u1})
        
    except:
        return redirect('login')    
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        # try:
            u1=SocietyMembers.objects.get(Email=request.POST['email'])
            request.session['email']=request.POST['email']
            return render(request,'dashboard.html',{"userdata":u1})
        # except:
            # return render(request,'login.html',{"msg":'email does not exist'})    
def myprofile(request):
    try:
        u1=SocietyMembers.objects.get(Email=request.session['email'])
        return render(request,'myprofile.html',{'userdata':u1}) 
    except:
        return redirect('login')    
def visitors3(request):
    try:
         u1=SocietyMembers.objects.get(Email=request.session['email'])
         u2=Visitor.objects.all()
         return render(request,'visitors3.html',{'visi':u2})

    except:
        return render(request,'login.html')

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:

        SocietyMembers.objects.create(
            first_name=request.POST['first_name'],
            Last_name=request.POST['Last_name'],
            Email=request.POST['email'],
            House_no=request.POST['House_no'],
            no_of_members=request.POST['no_of_members'],
            picture_of_owner=request.FILES['picture'],
            block_no=request.POST['block_no']
        ) 
        return render(request,'login.html')   
def logout(request):
    del request.session['email']
    return redirect('login')

def membersevent(request):
    try:
        u1=SocietyMembers.objects.get(Email=request.session['email'])
        u2=Events.objects.all()
        return render(request,'membersevent.html',{"events":u2})

    except:
        return render(request,'login.html')   

def notice_members(request):
    try:
        u1=SocietyMembers.objects.get(Email=request.session['email'])
        u2=Notice.objects.all()
        return render(request,'members_notice.html',{"notice":u2})

    except:
        return render(request,'login.html')  







# --------> secretory page <-------------------------------



def secretory_dashboard(request):
    try:
        
        u1=SocietySecretory.objects.get(email=request.session['email'])
        return render(request,'secretory_dashboard.html',{'userdata':u1})
        
    except:
        return redirect('secretorylogin')    
            
        
def secretorylogin(request):
    if request.method=='GET':
        return render(request,'secretorylogin.html')
    else:
        try:
            u1=SocietySecretory.objects.get(email=request.POST['email'])   
            request.session['email']=request.POST['email'] 
            return render(request,'secretory_dashboard.html',{"userdata1":u1})      

        except:
            return render(request,"secretorylogin.html",{'msg':"email does not exist"})      

# g

def secretory_profile(request):
    try:
        u1=SocietySecretory.objects.get(email=request.session['email'])
        return render(request,'secretory_profile.html',{'userdata':u1}) 
    except:
        return redirect('secretory_login')       

def secretory_register(request):
    if request.method=='GET':
        return render(request,'secretory_register.html')
    else:

        SocietySecretory.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            
            picture=request.FILES['picture']
        ) 
        return render(request,'secretorylogin.html')
def visitors2(request):
    try:
         u1=SocietySecretory.objects.get(email=request.session['email'])
         u2=Visitor.objects.all()
         return render(request,'visitors2.html',{'visi':u2})

    except:
        return render(request,'secretorylogin.html')
def secretory_logout(request):
    del request.session['email']
    return redirect('secretorylogin')

def society_members(request):
    try:
        u1=SocietySecretory.objects.get(email=request.session['email']) 
        u2=SocietyMembers.objects.all()
        return render(request,'society_membes.html',{'members':u2,'userdata':u1})

    except:
        return redirect('secretorylogin')    

def eventadd(request):
    if request.method=="GET":

        return render(request,'eventsadd.html')
    else:
        # u1=SocietyMembers.objects.get()
        # u1=Events.objects.get(id=request.POST['visited'])
        Events.objects.create(
            event_name =request.POST['event_name'],
            event_des =request.POST['event_des'],
            event_date=request.POST['event_date']
        )

        return render(request,'eventsadd.html',{"msg":"successfully added"})   
 
def noticeadd(request):
    if request.method=="GET":

        return render(request,'noticeadd.html')
    else:
        # u1=SocietyMembers.objects.get()
        # u1=Events.objects.get(id=request.POST['visited'])
        Notice.objects.create(
            notice_title =request.POST['notice_title'],
            notice_des =request.POST['notice_des'],
            notice_date=request.POST['notice_date']
        )

        return render(request,'noticeadd.html',{"msg":"successfully added"}) 

    
def society_watchman(request):
    try:
        u1=SocietySecretory.objects.get(email=request.session['email'])
        u2=Watchmen.objects.all()
        return render(request,'society_watchman.html',{"data":u2})

    except:
        return render(request,'secretorylogin.html') 

        #  ------------------> watchman page <---------------------------

def watchman_login(request):
    if request.method=='GET':
        return render(request,'watchman_login.html')
    else:
        try:
            u1=Watchmen.objects.get(email=request.POST['email'])   
            request.session['email']=request.POST['email'] 
            return render(request,'watchman_profile.html',{"userdata1":u1})      

        except:
            return render(request,"watchman_login.html",{'msg':"email does not exist"})  

            


def watchman_logout(request):
    del request.session['email']
    return redirect('watchman_login')

def watchman_profile(request):
    try:
        u1=Watchmen.objects.get(email=request.session['email'])
        return render(request,'watchman_profile.html',{'userdata':u1}) 
    except:
        return redirect('watchman_login')      

def watchman_dashboard(request):
    try:
        u1=Watchmen.objects.get(email=request.session['email'])
        return render(request,'watchman_dashboard.html',{'userdata':u1}) 
    except:
        return redirect('watchman_login')      
def society_members2(request):
    # try:
         u1=Watchmen.objects.get(email=request.session['email'])
         u2=SocietyMembers.objects.all()
         return render(request,'society_members2.html',{'members':u2})

    # except:
        # return render(request,'watchman_login.html')
def visitors(request):
    if request.method=="GET":

        return render(request,'visitors.html')
    else:
        # u1=SocietyMembers.objects.get()
        u1=SocietyMembers.objects.get(id=request.POST['visited'])
        Visitor.objects.create(
            v_name =request.POST['name'],
            v_contact =request.POST['contact_no'],
            member =u1
        )

        return render(request,'visitors.html',{"msg":"successfully added"})    


    

def watchman_register(request):
    if request.method=='GET':
        return render(request,'watchman_register.html')
    else:

        Watchmen.objects.create(
            watchmen_name=request.POST['name'],
            contact_no=request.POST['contact'],
            email=request.POST['email'],
            watchman_picture=request.FILES['picture']
        ) 
        return render(request,'watchman_login.html')   

def watchmanevent(request):
    try:
        u1=Watchmen.objects.get(email=request.session['email'])
        u2=Events.objects.all()
        return render(request,'watchmanevents.html',{"events":u2})

    except:
        return render(request,'watchman_login.html') 

def notice_watchman(request):
    
    try:
        u1=Watchmen.objects.get(email=request.session['email'])
        u2=Notice.objects.all()
        return render(request,'watchman_notice.html',{"notice":u2})

    except:
        return render(request,'watchman_login.html')  



