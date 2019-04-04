from django.shortcuts import render
from .models import HostGroup, Module

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    if request.method == 'POST':
        group_name = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group_name:  # 如果group不是空串
            group = HostGroup.objects.get_or_create(group_name=group_name)[0]
            if host and ip:  # 如果host和ip也都不是空串
                group.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def addmodules(request):
    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})
