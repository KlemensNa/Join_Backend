from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from Backend.models import Contact, Task
from Backend.serializer import ContactSerializer, TaskSerializer
from django.contrib.auth.models import User
from rest_framework import status




#Endpoint to view --> wird seperat mit eigenen Befehlen im Frontend angesprochen

# @method_decorator(csrf_exempt, name='dispatch')
class LoginView(ObtainAuthToken):    
    """
        serializer take request.data(email & password or username & password)
        proof if .isvalid --> not? then raise_exceptionError
        isvalidated, then get user from post.request, password muss nicht extra getestet werden
        token wird geholt oder neu erstellt
    """    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        #test mit Postman gibt Token zurück
        return Response({
            'token': token.key,
            'username': user.username
        })  
                

class TaskView(APIView):    
    #Authentication with token
    # permission only when authentication is successful
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()          
                return Response(serializer.data)
        return Response(serializer.errors)
    

class RegisterView(APIView):
    
    def post(self, request, format=None):
        user = User.objects.create_user(username=request.data.get('username'),
                                 email=request.data.get('email'),
                                 password=request.data.get('password'))
        token, created = Token.objects.get_or_create(user=user)        
        
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email
        })
        

class ContactView(APIView):
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Speichert das Contact-Objekt in der Datenbank
            return Response(serializer.data, status=201)  # Erfolgreiche Antwort
        return Response(serializer.errors, status=400)  # Fehlerhafte Daten
    
    
    def get(self, request, pk=None, format=None):
        if pk:
            try:
                contact = Contact.objects.get(pk=pk)
            except Contact.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
    
    
    def put(self, request, pk, format=None):
        try:
            contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        try:
            contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

        
