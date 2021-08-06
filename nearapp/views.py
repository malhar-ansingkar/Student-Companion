from pprint import pprint
from django.db.models import query
from django.shortcuts import render, HttpResponse
from .models import college, shop, PostImage, faqs
# Create your views here.
from django.views.generic.detail import DetailView
from django.core import serializers
from django.http import JsonResponse, response
from .filters import shopFilters
from django.db.models.functions import Length
import json
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializers import ShopSerializer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import filters
from .models import suggestionsForm
from .chatbotModel.bot import predict_class, get_response, intents


def index(request):
    form = suggestionsForm()
    if request.method == 'POST':
        form = suggestionsForm(request.POST)
        form.save()
    context = {}
    colleges = college.objects.all()
    context["colleges"] = colleges
    context["form"] = form

    return render(request, 'landing.html', context)


def filterPage(request, pk):
    collge = college.objects.get(pk=pk)
    shops = shop.objects.filter(college=collge)
    colleges = college.objects.all()

    context = {
        'college': collge,
        'shops': shops
    }
    context["colleges"] = colleges

    return render(request, 'landing1.html', context)


def typefilterPage(request, pk, type):
    collge = college.objects.get(pk=pk)
    shops = shop.objects.filter(college=collge, Type=type)
    colleges = college.objects.all()

    context = {
        'college': collge,
        'shops': shops,
        "type": type}
    # print(shops)
    context["colleges"] = colleges

    return render(request, 'new-filter1.html', context)


def detailsPage(request, pk):
    # collge =
    shops = shop.objects.get(pk=pk)
    images = PostImage.objects.filter(post=shops)
    colleges = college.objects.all()

    context = {
        'shop': shops,
        'images': images


    }
    context["colleges"] = colleges
    print(pk, type)

    return render(request, 'details.html', context)


# def filterApi(request, pk):
    import json
    import pprint

    lst = list((json.loads(request.body.decode("utf-8"))).values())
    shops = shop.objects.filter(pk=pk).order_by()

    context = {
        'shop': serializers.serialize("json", shops),

    }
    print(pprint.pprint(context, indent=4))
    # print(pk, type)
    return JsonResponse(context)

    # return render(request, 'details.html', context)


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def filterApi(request):
    js = {
        "Data": ""
    }
    if request.method == 'POST':

        # gst = '24AEAPS9376R2ZI'
        print(request.data)

        college = request.data["college"]
        filterType = request.data["filters"]

        if filterType == "Amenities":
            filterType = Length('Amenities').desc()

        if request.data["type"]:
            shops = shop.objects.filter(college=int(
                college), Type=request.data["type"]).order_by(filterType)

        js = {

            "Data": serializers.serialize("json", shops),
        }

    return Response(js)


def suggestions(request):
    form = suggestionsForm()
    if request.method == 'POST':
        form = suggestionsForm(request.POST)
        form.save()
    context = {}
    colleges = college.objects.all()

    context["form"] = form
    context["colleges"] = colleges

    return render(request, 'suggestions.html', context)


def faq(request):
    colleges = college.objects.all()
    faqz = faqs.objects.all()
    context = {'faqs': faqz, }
    context["colleges"] = colleges

    return render(request, 'FAQ.html', context)


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def chat(request):
    js = {
        'message': ""
    }

    if request.method == 'POST':
        print(request.data)
        data = request.data["message"]

        message = data
        ints = predict_class(message)
        res = get_response(ints, intents)
        # print(f'God:{res}')

        js['message'] = res

    return Response(js)


def train():
    allShops = shop.objects.all()

    with open('demo.json') as f:
        data = json.load(f)
    data = {}
    pattrenEnt = {'patterns': [],
                  'responses': [],
                  'tag': 'greeting'}
    lst = data["intents"]

    for i in range(10):
        lst.append({'patterns': [i],
                    'responses': [i],
                    'tag': 'greeting'})

    print(pprint(lst))


def aboutUs(request):
    colleges = college.objects.all()
    context = {}
    context["colleges"] = colleges

    return render(request, 'about-us.html', context)


# @api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
# def getAllCollegs(request):
#     colleges = college.objects.all()
#     return response({"col": colleges})
