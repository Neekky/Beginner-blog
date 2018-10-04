from django.db import models

# Create your models here.
# 数据模块，数据表都在这里创建，ORM框架
# 对应数据库的一张表
'''
ORM
    对象关系映射（Object Relation Mapping)
    实现了对象和数据库之间的映射
    隐藏了数据访问的细节，不需要编写SQL语句
'''

class Article(models.Model):
    title = models.CharField(max_length = 32,default = 'Title')
    content = models.TextField(null=True)

    def __str__(self):
        return self.title
