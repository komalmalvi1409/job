from django.urls import path
from .import views
from .views import HrJobCreate
from .views import HrJobList
from .views import HrJobDetailView,HrJobUpdate,HrJobDelete

urlpatterns=[

    path('hrjobcreate', HrJobCreate.as_view()),
    path('hrjoblist', HrJobList.as_view()),
    path('<pk>/', HrJobDetailView.as_view()),
    path('<pk>/update', HrJobUpdate.as_view()),
    path('<pk>/delete', HrJobDelete.as_view()),
    path('dashboard',views.dashboard,name="dashboard"),
    path('hrregistr',views.hrregistr,name="hrregistr"),
    path('hrlogin',views.hrlogin,name='hrlogin'),
    path('hrlogout',views.hrlogout,name='hrlogout'),
    path('job',views.job,name='job'),
    path('candidate',views.candidate,name='candidate'),
    path('checkuser',views.checkuser,name='checkuser'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('resume1',views.resume1,name='resume1'),
    path('candidateinfo',views.candidateinfo,name='candidateinfo')
    
  

]