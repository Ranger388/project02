from django.db import models

class Department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name="标题",max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    #create_time = models.DateTimeField(verbose_name="入职时间")
    create_time = models.DateField(verbose_name="入职时间")
    #外键关联部门表
    #1.约束
    #2.自动补名
    #3.级联删除
    depart = models.ForeignKey(verbose_name="部门",to='Department',to_field='id',on_delete=models.CASCADE)
    #4.置空删除
    #depart = models.ForeignKey(to='Department',to_field='id',null=True,blank=True,on_delete=models.SET_NULL)
    #性别
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

class PrettyNum(models.Model):
    """ 靓号表 """
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0)
    level_choices = ((1,'普通'),(2,'史诗'),(3,'传说'),(4,'仙品'))
    level = models.SmallIntegerField(verbose_name="等级", choices=level_choices, default=1)
    status = models.SmallIntegerField(verbose_name="状态", choices=((1,'已占用'),(2,'未占用')), default=2)

class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)