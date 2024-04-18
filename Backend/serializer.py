from rest_framework import serializers
from .models import Category, Contact, Subtask, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = '__all__'
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print("Serialized contact:", representation)  # Debug-Ausgabe hinzufügen
        return representation
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class SubtasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'
        
        
class TaskPOSTSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Task
        fields = '__all__'
        

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = ContactSerializer(many=True)
    category = CategorySerializer()
    subtasks = SubtasksSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'
        
        


    

        
