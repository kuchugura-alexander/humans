# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import HumanSerializer  # UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Human


def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

@csrf_exempt
def humans_list(request):
    """
    List all humans.
    """
    if request.method == "GET":
        factory = APIRequestFactory()
        request = factory.get('/')

        serializer_context = {
            'request': Request(request),
        }

        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False
                            , json_dumps_params={'ensure_ascii': False})
    # elif request.method == "POST":
    #     data = JSONParser().parse(request)
    #     serializer = HumanSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def human_detail(request, pk):
    """
    Retrieve, update or delete a Human.
    """
    try:
        human = Human.objects.get(pk=pk)
    except Human.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HumanSerializer(human)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HumanSerializer(human, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        human.delete()
        return HttpResponse(status=204)
