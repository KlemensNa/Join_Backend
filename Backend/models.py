from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 10)
    
    def __str__(self) -> str:
        return self.name
         

class Contact(models.Model):
    name = models.CharField(max_length = 40)
    phone = models.CharField(max_length = 30)
    email = models.CharField(max_length = 40)
    acronym = models.CharField(max_length = 10)
    color = models.CharField(max_length = 10)    
    
    #name in adminMenu wird zurückgegeben
    def __str__(self) -> str:
        return self.name
    


class Subtask(models.Model):
    name = models.CharField(max_length = 30)
    checked = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.name
    
    
class Task(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    category = models.ForeignKey(
        Category,
        on_delete = models.PROTECT
    )
    assigned_to = models.ManyToManyField(Contact)
    due_date = models.DateField()
    prio = models.CharField(max_length = 10)
    column = models.CharField(max_length = 30, default="board_container_bottom_todo")
    subtasks = models.ManyToManyField(Subtask, null=True, default=[], blank=True)
    
    #title in adminMenu wird zurückgegeben
    def __str__(self) -> str:
        return self.title
    





    