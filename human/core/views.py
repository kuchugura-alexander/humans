# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import HumanSerializer  # UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Human
from rest_framework import status


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


@api_view(['GET'])
@csrf_exempt
def humans_list(request):
    """
    List all humans.
    """
    if request.method == "GET":
        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    # elif request.method == "POST":
    #     data = JSONParser().parse(request)
    #     serializer = HumanSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
@csrf_exempt
def human_detail(request, pk):
    """
    Retrieve, update or delete a Human.
    """
    try:
        human = Human.objects.get(pk=pk)
    except Human.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HumanSerializer(human)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HumanSerializer(human, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        human.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
