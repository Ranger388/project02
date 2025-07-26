from django.shortcuts import render,HttpResponse
import os
from app01 import models
from django import forms
from app01.utils.bootstrap import BootStrapForm, BootStrapForm, BootStrapModelForm
from django.conf import settings


def upload_list(request):
    if request.method == "GET":
        return render(request, 'upload_list.html')

    file_object = request.FILES.get("avatar")
    f = open(file_object.name, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()

    return HttpResponse("...")

class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ["img"]
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")

def upload_form(request):
    title = "Form上传"
    if request.method == "GET":
        form = UpForm()
        return render(request, 'upload_form.html', {'form': form, "title": title})

    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        #读到内容，自己处理每个字段的数据
        #1.读取图片内容，写入到文件夹中并获取文件的路径
        image_object = form.cleaned_data.get("img")
        #media_path = os.path.join(settings.MEDIA_ROOT, image_object.name)
        media_path = os.path.join("media", image_object.name)
        f = open(media_path, mode='wb')
        #.chunk()方法是openpyxl里的
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()

        #2.将图片文件路径写入到数据库
        models.Boss.objects.create(
            name=form.cleaned_data["name"],
            age=form.cleaned_data["age"],
            img=media_path,
        )
        return HttpResponse("...")
    return render(request, 'upload_form.html', {'form': form, "title": title})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]
    class Meta:
        model = models.City
        fields = "__all__"

def upload_model_form(request):
    """ 上传文件和数据 (modelForm)"""
    title = "ModelForm上传文件"
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {'form': form, "title": title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        #对于文件，自动保存
        #字段+上传路径写入到数据库
        form.save()
        return HttpResponse("成功")
    return render(request, 'upload_form.html', {'form': form, "title": title})