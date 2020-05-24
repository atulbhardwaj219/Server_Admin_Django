from django.shortcuts import render
from .forms import AddServer
from .models import Servers,Request
import paramiko
from django.shortcuts import render
import time
from .tasks import *


from django.shortcuts import redirect
from django.contrib import messages
import subprocess
# Create your views here


def home1(request):
    s=Request.objects.all()
    queue=0
    completed=0
    inprogress=0
    failed=0

    for s in s:
        if s.status=='Queue':
            queue=queue+1
        if s.status=='Completed':
            completed=completed+1
        if s.status=='Inprogress':
            inprogress=inprogress+1
        if s.status=='Failed':
            failed=failed+1




    return render(request, 'home.html',{'sv':s,'queue':queue,'completed':completed,'inprogress':inprogress,'failed':failed})

def CreateInstance(request):
    if request.method=='POST':
        form=AddServer(request.POST)
        msg=request.POST.get('password2')

        if form.is_valid():
            form.save()
            msg= 'Server Added successfully'
            return render(request, 'createinstance.html',{'form':form,'msg':msg})
        else:
            form=AddServer(request.POST)

            return render(request, 'createinstance.html',{'form':form,'msg':form.errors})

    form=AddServer()
    msg="Add server"
    return render(request, 'createinstance.html',{'form':form,'msg':msg})

def ShowInstances(request):

    s=Servers.objects.all()
    return render(request, 'showinstances.html',{'sv':s})


def StartStop(request):
    s=Servers.objects.all()
    if request.method=='POST':
        msg=request.POST.get('instancename')
        msg=msg.split(" -- ")
        print("msg is",msg[0])
        action=request.POST.get('action')


        d=Servers.objects.get(Instancename=msg[0])
        requests=Request(Instancename=d.Instancename,ip=d.ip,status='Queue', request= action)
        requests.save()



        latest=Request.objects.latest('id')
        print (latest.id)
        latestid=str(latest.id)

        print("Latest ID is  :",latestid)


        y=startstop.delay(d.ip,d.port,d.username,d.password,latestid,action)
        print("yo",y)
        messages.success(request, 'Show Progress by go to Request History Page')
        return redirect('home1')

    msg=""
    return render(request, 'startstop.html',{'sv':s,'msg':msg})




def RequestHistory(request):
    s=Request.objects.all()
    return render(request, 'requesthistory.html',{'sv':s})



# Create your views here.
