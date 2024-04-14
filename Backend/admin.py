from django.contrib import admin
from Backend.models import Category, Contact, Subtask, Task

admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Subtask)

