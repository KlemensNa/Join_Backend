from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from Backend.models import Task
from Backend.serializer import TaskSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt




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
            'user_id': user.pk,
            'email': user.email
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
        user = User.objects.create_user(username=request.POST.get('registerName'),
                                 first_name=request.POST.get('Firstname'), 
                                 last_name=request.POST.get('Lastname'), 
                                 email=request.POST.get('registerEmail'),
                                 password=request.POST.get('registerPassword'))
        
        
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()          
                return Response(serializer.data)
        return Response(serializer.errors)
    
    
    
    
    
    # if request.method == "POST":
        
    #     return render(request, 'auth/login.html', {'redirect': redirect})
    # return render(request, 'register/register.html', {'redirect': redirect, 'Greeting' : False, 'SignIn' : True})


        
