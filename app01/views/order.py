from django.shortcuts import render
from django.http import JsonResponse
from app01.utils.bootstrap import BootStrapModelForm
from app01 import models
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from app01.utils.pagination import Pagination
import random

class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = '__all__'
        exclude = ["oid", "admin"]


def order_list(request):
    queryset = models.Order.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm()

    context = {
        'form': form,
        'page_string': page_object.html(),
        'queryset': page_object.page_queryset,
    }

    return render(request, 'order_list.html', context)

@csrf_exempt
def order_add(request):
    """ 新建订单(Ajax请求) """
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        #生成订单号
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000,9999))

        #固定设置管理员ID,从session中获取信息
        form.instance.admin_id = request.session["info"]["id"]



        #保存
        form.save()
        return JsonResponse( {'status': True} )

    return JsonResponse( {'status': False, 'error': form.errors} )

def order_delete(request):
    """ 删除订单 """
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse( {'status': False, 'error': '数据不存在' } )

    models.Order.objects.filter(id=uid).delete()
    return JsonResponse( {'status': True} )

def order_detail(request):
    """ 根据ID获取订单详细 """


    #方式1
    # uid = request.GET.get('uid')
    # row_object = models.Order.objects.filter(id=uid).first()
    # if not row_object:
    #     return JsonResponse( {'status': False, 'error': '数据不存在' } )
    #
    # result = {
    #     'status': True,
    #     "data": {
    #         "title": row_object.title,
    #         "price": row_object.price,
    #         "status": row_object.status,
    #     }
    # }
    # return JsonResponse(result)


    #方式2
    uid = request.GET.get('uid')
    row_dict = models.Order.objects.filter(id=uid).values("title","price","status").first()
    if not row_dict:
        return JsonResponse({'status': False, 'error': '数据不存在'})

    result = {
        'status': True,
        "data": row_dict,
    }

    return JsonResponse(result)

@csrf_exempt
def order_edit(request):
    """ 编辑订单 """
    uid = request.GET.get('uid')
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({'status': False, 'tips': '数据不存在'})

    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse( {'status': True} )

    return JsonResponse( {'status': False, 'error': form.errors} )