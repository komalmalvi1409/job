from django.db import models
from django.db.models import Model


class Registration(models.Model):
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)  
    password=models.CharField(max_length=50) 
    mobileno=models.CharField(max_length=10) 
    technology=models.CharField(max_length=20)
    candidatetype=models.CharField(max_length=20)
    higherqulification=models.CharField(max_length=40)
    passingyear=models.CharField(max_length=100)

class Hrregistration(models.Model):
    email = models.CharField(max_length=100)  
    password=models.CharField(max_length=50) 
    mobileno=models.CharField(max_length=10) 
    companyname= models.CharField(max_length=100)  

class Hrjob(models.Model):
    jobtitle=models.CharField(max_length=50)
    jobdescription=models.CharField(max_length=250)
    experience=models.CharField(max_length=40)
    uploadimag=models.ImageField()
    technology=models.CharField(max_length=40)
    postdate=models.CharField(max_length=40)
    duedate=models.CharField(max_length=40)

class Candidate(models.Model):
    email = models.CharField(max_length=100)   
    jobid=models.CharField(max_length=50) 
    applydate=models.CharField(max_length=60)
    name=models.CharField(max_length=70)



class Resume(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    job_city = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    
    Objective = models.CharField(max_length=50)
    Workexperience = models.CharField(max_length=500)
    ITSKILLS = models.CharField(max_length=500)
    
    HOBBIESINTEREST = models.CharField(max_length=500)
    DECLARATION = models.CharField(max_length=500)
    
    percentage = models.CharField(max_length=500)
    branch = models.CharField(max_length=50)
    Passingyear = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    univercity = models.CharField(max_length=50)
    dpercentage = models.CharField(max_length=500)
    dbranch = models.CharField(max_length=50)
    dPassingyear = models.CharField(max_length=50)
    dcourse = models.CharField(max_length=50)
    dunivercity = models.CharField(max_length=50)
    gpercentage = models.CharField(max_length=500)
    gbranch = models.CharField(max_length=50)
    gPassingyear = models.CharField(max_length=50)
    gcourse = models.CharField(max_length=50)
    gunivercity = models.CharField(max_length=50)
    pgpercentage = models.CharField(max_length=500)
    pgbranch = models.CharField(max_length=50)
    pgPassingyear = models.CharField(max_length=50)
    pgcourse = models.CharField(max_length=50)
    pgunivercity = models.CharField(max_length=50)