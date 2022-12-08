from django.contrib import admin
from myfiles.models import *
# Register your models here.
class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','nomi','tur','rasm']
admin.site.register(Portfolio,AdminPortfolio)


class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Type,AdminType)

class AdminTeam(admin.ModelAdmin):
    list_display = ['id','rasm','ism','ishi','matn','skype','instagram','facebook','linked']
admin.site.register(Team,AdminTeam)


class AdminService(admin.ModelAdmin):
    list_display = ['id','rasmi','nomi','matni']
admin.site.register(Service,AdminService)

class AdminMessage(admin.ModelAdmin):
    list_display = ['id','ismi','mail','subject','message','time']
admin.site.register(Message,AdminMessage)