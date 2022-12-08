from django.shortcuts import render
from myfiles.models import *
# Create your views here.
def home(malumot):
    if malumot.method=='POST':
        ism = malumot.POST.get('name')
        mail = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        message = malumot.POST.get('message')
        Message(ismi=ism,mail=mail,subject=subject,message=message).save()
    turlar = Type.objects.all()
    team = Team.objects.all
    portfolio = Portfolio.objects.all()
    servis = Service.objects.all()
    return render(malumot,'index.html',{'kalit':portfolio,'turlar':turlar,'rasm':team,'servis':servis})

def filter_index(malumot,turlar):
    portfolio = Portfolio.objects.filter(tur_id=turlar)
    turis = Type.objects.all()
    return render(malumot,'index.html',{'kalit':portfolio,'turlar':turis})

