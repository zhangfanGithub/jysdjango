from django.db import models
from  datetime import  datetime
# Create your models here.
class ProInfo(models.Model):
    '''每个省信息'''
    #省名
    pro_name = models.CharField(max_length=20)
    #省面积
    pro_size = models.CharField(max_length=100)
    #数据记录日期
    pro_update_time = models.DateField()

    def __str__(self):
        return self.pro_name

class City(models.Model):
    '''city 每一个城市'''
    #城市名称
    city_name = models.CharField(max_length=20)
    #城市等级
    city_grad = models.IntegerField()
    #城市人口
    city_person_num = models.IntegerField()
    #城市外键省
    city_proname = models.ForeignKey('ProInfo',on_delete=models.CASCADE,)
    def __str__(self):
        return self.city_name