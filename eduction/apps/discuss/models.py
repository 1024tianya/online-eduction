from django.db import models
from datetime import datetime


# Create your models here.

class Room(models.Model):
    name = models.CharField("房间名称", max_length=100)
    wx_url = models.URLField("房间链接")
    add_time = models.DateTimeField("添加时间", default=datetime.now)
    update = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "全部房间"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name