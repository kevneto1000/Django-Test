from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ResgisterationSerializer
from .models import Registeration, Register

# Create your views here.

@api_view(['POST'])
def register(request):

    serializer = ResgisterationSerializer(data=request.data)


    try:

        serializer.is_valid()
        serializer.save()
        return Response("User Created Successfully", status=201)
    
    except Exception as e:
        return Response( str(e), status=400)
    
@api_view(['GET'])
def verifyuser(request, id):
    register = Registeration.objects.filter(id = id).first()

    if register is None:
        return Response(data="Invalid", status=400)
    
    else:
        register.is_active = True
        register.save()
        
        return Response("your account is verified", status=200)

@api_view(['POST'])
def registeration(request):

    serializer 
