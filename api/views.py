from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Commands, Articles
from .serializers import CommandsSerializer, ArticlesSerializer

from rest_framework import status


# Create your views here.
@api_view()
def commands(request):
    queryset = Commands.objects.all()
    serializer = CommandsSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def commandsid(request, id):
    command = get_object_or_404(Commands, pk=id)
    serializer = CommandsSerializer(command)

    return Response(serializer.data)



@api_view()
def articles(request):
    queryset = Articles.objects.all()
    serializer = ArticlesSerializer(queryset, many=True)
    return Response(serializer.data)
