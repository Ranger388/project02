from django.shortcuts import render
from django.http import JsonResponse


def chart_list(request):
    """ 数据统计页面 """
    return render(request, "chart_list.html")


def chart_bar(request):
    """ 构造柱状图的数据 """
    legend = ["A", "B"]

    series_list = [
        {
            "name": 'A',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
        },
        {
            "name": 'B',
            "type": 'bar',
            "data": [15, 120, 136, 110, 110, 120]
        }
    ]

    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }

    return JsonResponse(result)


def chart_pie(request):
    """ 构造饼状图的数据 """
    db_data_list = [
        {"value": 1048, "name": 'IT部门'},
        {"value": 735, "name": '运营'},
        {"value": 580, "name": '新媒体'},
    ]

    result = {
        "status": True,
        "data": db_data_list,
    }

    return JsonResponse(result)


def chart_line(request):
    """ 构造折线图的数据 """
    legend = ["上海", "广西"]

    series_list = [
        {
            "name": '广西',
            "type": 'line',
            "stack": 'Total',
            "data": [11, 80, 76, 69, 89, 110],
        },
        {
            "name": '上海',
            "type": 'line',
            "stack": 'Total',
            "data": [15, 120, 136, 110, 110, 120],
        },
    ]

    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }

    return JsonResponse(result)

def highcharts(request):
    """ highcharts """
    return render(request,'highcharts.html')