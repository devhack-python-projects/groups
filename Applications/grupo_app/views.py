from django.shortcuts import render
from django.views import generic
from django import http
from django.views.decorators.csrf import csrf_exempt
import jwt
import requests
import json

class RxHeader(generic.View):

    def get(self,request,*args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION", "")
        token = token.replace("JWT ", "")
        response = requests.get("http://ma0collazos.pythonanywhere.com/verify/", headers={"authorization": token})
        print(response.content)
        print(response.status_code)
        if response.status_code == 201:
            #return http.HttpResponse(token)
            decoded = jwt.decode(token, verify=False)
            return http.HttpResponse(json.dumps(decoded))
        else:
            return http.HttpResponse("asd",status = 404)
        # return http.HttpResponse(request.META["HTTP_AUTHORIZATION"])
# Create your views here.
class RxHeader2(generic.View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(RxHeader2, self).dispatch(request, *args, **kwargs)


    def post(self,request,*args, **kwargs):
        return http.HttpResponse("hello worldddd")

        #return http.HttpResponse(request.META.get("HTTP_AUTHORIZATION", ""))
