from django.db import models
from django.http import HttpResponse
from datetime import datetime

class ToDoList(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    desc = models.TextField(null=True)
    creatorId = models.BigIntegerField(null=False)
    createdTime = models.DateTimeField(null=False)

    def __str__(self):
        return str(self.createdTime) + " " +str(self.creatorId) + " " + self.title


def create_to_do_list(request):
    from account.models import isLogged
    if not isLogged(request):
        return HttpResponse('{"result":"fail"}')
    tdl = ToDoList()
    tdl.title = request.POST.get('title', 'No Title')
    tdl.date = request.POST.get('date', datetime.now())
    tdl.time = request.POST.get('time', '00:00')
    tdl.desc = request.POST.get('desc', '')
    tdl.creatorId = request.session['uid']
    tdl.createdTime = datetime.now()
    tdl.save()
    return HttpResponse('{"result":"pass", "headto":"#r"}')


def deltdl(request):
    from account.models import isLogged
    if not isLogged(request):
        return HttpResponse("oops")
    id = request.POST.get('id', '#')
    if id != '#':
        ToDoList.objects.get(id=id).delete()
        return HttpResponse("deleted")
    return HttpResponse("opps")


def getAllList(request):
    tdl = ToDoList.objects.filter(creatorId=request.session['uid'])
    return tdl