from django.contrib import admin
from sc.models import  ProInfo,City
# Register your models here.

#省页面管理类
class ProInfoAdmin(admin.ModelAdmin):
    list_display = ['pro_name','pro_size','pro_update_time']


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name','city_grad','city_person_num','city_proname']
admin.site.register(ProInfo, ProInfoAdmin)
admin.site.register(City, CityAdmin)
