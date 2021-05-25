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
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

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


class HumansList(APIView):
    """
    List all humans.
    """
    def get(self, request, format=None):
        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True)
        return Response(serializer.data)
    # elif request.method == "POST":
    #     data = JSONParser().parse(request)
    #     serializer = HumanSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HumanDetail(APIView):
    """
    Retrieve, update or delete a Human.
    """
    def get_object(self, pk):
        """
        Prepare before launch methods of the class.
        """
        try:
            return Human.objects.get(pk=pk)
        except Human.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        """
        Retrieve.
        """
        human = self.get_object(pk)
        serializer = HumanSerializer(human)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Create and Update.
        """
        human = self.get_object(pk)
        serializer = HumanSerializer(human, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete.
        """
        human = self.get_object(pk)
        human.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
