from rest_framework import serializers
from .models import Category, Contact, Subtask, Task




        
        
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

    def update(self, instance, validated_data):
        assigned_to_data = validated_data.pop('assigned_to', None)
        subtasks_data = validated_data.pop('subtasks', None)

        instance = super().update(instance, validated_data)

        if assigned_to_data is not None:
            instance.assigned_to.set(assigned_to_data)

        if subtasks_data is not None:
            instance.subtasks.clear()  # Clear existing subtasks
            for subtask_data in subtasks_data:
                subtask, created = Subtask.objects.get_or_create(**subtask_data)
                instance.subtasks.add(subtask)

        return instance
    

        
