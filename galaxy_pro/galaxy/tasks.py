
from celery import shared_task
import paramiko
from .models import Servers,Request



@shared_task
def startstop(ip,port,username,password,latestid,action):
    t = Request.objects.get(id=latestid)
    t.status ='Inprogress'
    t.save()
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip,port=port,username=username,password=password)
        t=paramiko.Transport((ip,port))
        t.connect(username=username,password=password)
    except Exception as e:
        action=action

        print('message is',e)
        t = Request.objects.get(id=latestid)
        t.status ='Failed'
        t.save()
        return 'Not able to ssh, Kindly check with machine'


    if action== 'start':
        # change field
        stdin, stdout, stderr=ssh.exec_command('sudo systemctl start crond')
        y=stdout.read()
       

        t = Request.objects.get(id=latestid)
        t.status ='Completed'
        t.save()
        return y

    if action== 'stop':

        stdin, stdout, stderr=ssh.exec_command("sudo systemctl stop crond")
        y=str(stdout.read())
        t = Request.objects.get(id=latestid)
        t.status ='Completed'  # change field
        t.save()
        return y

    if action== 'restart':
        stdin, stdout, stderr=ssh.exec_command("sudo systemctl restart crond")
        y=str(stdout.read())
        t = Request.objects.get(id=latestid)
        t.status ='Completed'  # change field
        t.save()
        return y

    if action== 'enable':
        stdin, stdout, stderr=ssh.exec_command("sudo systemctl enable crond")
        y=str(stdout.read())
        t = Request.objects.get(id=latestid)
        t.status ='Completed'  # change field
        t.save()
        return y

    return 'No data found'

