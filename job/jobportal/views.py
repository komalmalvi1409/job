from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration
from .models import Hrregistration
from .models import Hrjob
from .models import Candidate
from .models import Resume
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


def dashboard(request):
    return render(request,"jobportal/dashboard.html")


def hrregistr(request):
    if request.method=="POST":
        d=Hrregistration(email=request.POST["email"],password=request.POST["password"],mobileno=request.POST["mobileno"],companyname=request.POST["companyname"])
        d.save()
        return redirect("hrlogin")
        return render(request,"jobportal/hrregistration.html",{"msg": "data insert successfully"})
    return render(request,"jobportal/hrregistration.html")

def hrlogin(request):
  if request.method=="POST":
    d = Hrregistration.objects.filter(email=request.POST["email"],password=request.POST["password"])
    if d.count()>0:
        request.session["sessioniid"]=request.POST["email"]
        if request.POST.get("chk"):
            response = HttpResponse(status=302)
            response.set_cookie('ukey',request.POST["email"])
            response.set_cookie('upass',request.POST["password"])
            response['Location']='hrjobcreate'
            return  response
      
    else:
        return render(request,"jobportal/hrlogin.html",{"msg":"invalid userid and password"}) 
  else:
   c1=''
   c2=''
   if request.COOKIES.get('ukey'):
     c1=request.COOKIES["ukey"]
     c2=request.COOKIES["upass"]
   return render(request,"jobportal/hrlogin.html",{'ucookie':c1,'upass':c2})


class HrJobCreate(CreateView):
	model = Hrjob  
	fields = ['jobtitle', 'jobdescription','experience','uploadimag','technology','postdate','duedate']
	success_url = '/jobportal/hrjoblist'

class HrJobUpdate(UpdateView):
	model = Hrjob
	fields = ['jobtitle', 'jobdescription','experience','uploadimag','technology','postdate','duedate']
	success_url = '/jobportal/hrjoblist'

class HrJobDelete(DeleteView):
	model = Hrjob
	success_url = '/jobportal/hrjoblist'
	
class HrJobList(ListView):
	model = Hrjob


class HrJobDetailView(DetailView):
   model = Hrjob


       
def hrlogout(request):
   response= HttpResponse(status=302)
   response.delete_cookie('email',"/")
   response.delete_cookie('password',"/")
   del  request.session["sessioniid"]
   response['Location']='dashboard'
   return  response


def job(request):
    if (request.session.has_key('sessionid')):
        sid=request.session['sessionid']
        data=Hrjob.objects.all() 
        return render(request,"jobportal/job.html",{"d":data})
    else:    
        return redirect('login')

         

def registration(request):
    Degree=['Post Graduation','Graduation','Diploma','12th','10th']
    if request.method=="POST":
        d=Registration(name=request.POST["name"],email=request.POST["email"],password=request.POST["password"],
        mobileno=request.POST["mobileno"],technology=request.POST["technology"],candidatetype=request.POST["candidatetype"],
        higherqulification=request.POST["higherqulification"],passingyear=request.POST["passingyear"])
        d.save()
        return redirect("login")
        return render(request,"jobportal/registration.html",{"res2":Degree,"msg": "data insert successfully"})
    return render(request,"jobportal/registration.html",{"res2":Degree})

def checkuser(request):
	data = Registration.objects.filter(email=request.GET['q'])
	r= ''
	if data.count()>0:
		r = 'Userid already exist'
	else:
		r= ''		
	return HttpResponse(r)	    


     
def login(request):
  if request.method=="POST":
    d = Registration.objects.filter(email=request.POST["email"],password=request.POST["password"])
    if d.count()>0:
        request.session["sessionid"]=request.POST["email"]
        if request.POST.get("chk"):
            response = HttpResponse(status=302)
            response.set_cookie('ukey',request.POST["email"])
            response.set_cookie('upass',request.POST["password"])
            response['Location']='job'
            return  response
     
    else:
        return render(request,"jobportal/login.html",{"msg":"invalid userid and password"}) 
  else:
   c1=''
   c2=''
   if request.COOKIES.get('ukey'):
     c1=request.COOKIES["ukey"]
     c2=request.COOKIES["upass"]
   return render(request,"jobportal/login.html",{'ucookie':c1,'upass':c2})   

	  

def logout(request):
   response= HttpResponse(status=302)
   response.delete_cookie('email',"/")
   response.delete_cookie('password',"/")
   del  request.session["sessionid"]
   response['Location']='dashboard'
   return  response


def resume1(request):
    r1=None
    state=['select state',' ','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat',
    'Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra',
    'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
    'Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
    branch=['select','General','Mathematics','Biology','Automobile Engineering','Computer Science','Electronics & Communication ','Electrical Engineering','Mechanical ','Agricultural Engineering',
    'Architectural Engineering','Information Technology','Civil Engineering']
    year=['select','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
    course=['select','10th','12th','DIPLOMA','Graduation','PostGraduation','Phd']
    if request.method=="POST":
        
        r1 = Resume(name=request.POST["name"],gender=request.POST["gender"],
             city=request.POST["city"],pin=request.POST["pincode"],state=request.POST["state"],
             mobile=request.POST["mobileno"],email=request.POST["email"],job_city=request.POST["jobcity"],
             Address=request.POST["address"],Objective=request.POST["objetive"],
             Workexperience=request.POST["workexperience"],ITSKILLS=request.POST["itskill"],
             HOBBIESINTEREST=request.POST["hobbies"],DECLARATION=request.POST["declaration"],
             course=request.POST["hsc"],branch=request.POST["subject"],
             Passingyear=request.POST["passingyear1"],percentage=request.POST["percentage"],univercity=request.POST["board"],
             dcourse=request.POST["12th/diploma"],dbranch=request.POST["branch1"],
             dPassingyear=request.POST["passingyear2"],dpercentage=request.POST["percentage1"],dunivercity=request.POST["univercity1"],
             gcourse=request.POST["degree"],gbranch=request.POST["branch2"],
             gPassingyear=request.POST["passingyear3"],gpercentage=request.POST["percentage2"],gunivercity=request.POST["univercity2"],
            ) 
        r1.save()
        return render(request,"jobportal/resumeshow.html",{"y":year,"b":branch,"c":course,"res":state,"d":Resume.objects.filter(id=r1.id)})
    return render(request,"jobportal/resume.html",{"y":year,"b":branch,"c1":course,"res":state,"d":Resume.objects.all()})


def candidate(request): 
    
    can=Hrjob.objects.all()
    if request.method=="POST":
        r=Candidate(email=request.POST["email"],jobid=request.POST["ddljob"],applydate=request.POST["applydate"],name=request.POST["name"])
        r.save()
        return render(request,"jobportal/candidate.html",{"res":can,"msg":"data insert successfully"})  
    return render(request,"jobportal/candidate.html",{"res":can,"jid":(request.GET["q"])})


def candidateinfo(request):
    if request.method=="POST":
        c=Candidate.objects.filter(name=request.POST["name"])  
        return render(request,"jobportal/candidateinfo.html",{"d":c})  
    return render(request,"jobportal/candidateinfo.html",{"d":c})  
    