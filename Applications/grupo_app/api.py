from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
import requests
import json

from . import (
    models,
    serializers
)

class Groups(APIView):
    serializer_class = serializers.Group

    def get(self, request, *args, **kwargs):
        print(vars(request))
        groups = models.Group.objects.all()
        serializer = self.serializer_class(groups, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION", "")
        token = token.replace("JWT ", "")
        response = requests.get("http://ma0collazos.pythonanywhere.com/verify/", headers={"authorization": token})
        print(response.content)
        print(response.status_code)
        if response.status_code == 201:
            #return http.HttpResponse(token)
            decoded = jwt.decode(token, verify=False)

            serializer = self.serializer_class(data=self.request.POST)
            if serializer.is_valid():
                post = serializer.save()
                print(post)
                return Response(serializer.data, status=200)
            else:
                print("Error")
                print(serializer.errors)
                return Response(serializer.errors, status=400)
        else:
            return Response("error",status = 401)
#
#
# class PostWithId(APIView):
#
#     serializer_class = serializers.Post
#
#     def get(self, request, *args, **kwargs):
#         post_id = self.kwargs.get("id", "")
#         print(models.Post.objects.all())
#         post = get_object_or_404(models.Post, pk=post_id)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data, status=200)
#
#     def put(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=self.request.POST)
#         print(self.request.POST)
#         if serializer.is_valid():
#             post_id = self.kwargs.get("id", "")
#             post = get_object_or_404(models.Post, pk=post_id)
#             post.title = serializer.data.get("title", "")
#             post.body = serializer.data.get("body", "")
#             post.save()
#             return Response(serializer.data, status=200)
#         else:
#             print("Error")
#             print(serializer.errors)
#             return Response(serializer.errors)
#
#     def delete(self, request, *args, **kwargs):
#         post_id = self.kwargs.get("id", "")
#         post = get_object_or_404(models.Post, pk =post_id)
#         post.delete()
#         return Response({"status": "deleted"})
