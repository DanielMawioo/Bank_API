from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from .serializers import*

# Create your views here.
class BranchList(APIView):

    def get(self, request):
        branches = Branch.objects.all()
        serializer= BranchSerializer(branches, many= True)
        return Response(serializer.data)
