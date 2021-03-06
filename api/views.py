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

class BankList(APIView):

    def get(self, request):
        banks = Bank.objects.all()
        serializer= BranchSerializer(banks, many= True)
        return Response(serializer.data)

class ClientManagerList(APIView):

    def get(self, request):
        client_manager = ClientManager.objects.all()
        serializer= ClientManagerSerializer(client_manager, many= True)
        return Response(serializer.data)

class ClientList(APIView):

    def get(self, request):
        client = Client.objects.all()
        serializer= ClientSerializer(client, many= True)
        return Response(serializer.data)

class AccountList(APIView):

    def get(self, request):
        account = Account.objects.all()
        serializer= AccountSerializer(account, many= True)
        return Response(serializer.data)

class TransferList(APIView):

    def get(self, request):
        transfer = Transfer.objects.all()
        serializer= TransferSerializer(transfer, many= True)
        return Response(serializer.data)

class WithdrawList(APIView):

    def get(self, request):
        Withdraw = Withdraw.objects.all()
        serializer= WithdrawSerializer(Withdraw, many= True)
        return Response(serializer.data)

class DepositList(APIView):

    def get(self, request):
        deposit = Deposit.objects.all()
        serializer= DepositSerializer(deposit, many= True)
        return Response(serializer.data)
