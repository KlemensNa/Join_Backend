from datetime import datetime
import json
import pdb
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TaskTest(APITestCase):    
    
    def setUp(self):
        self.username = 'testuser'
        self.email = 'test@example.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    
    def test_create_subtask(self):
        data = {
            "name": "Test Subtask",
            "checked": False
        }
        
        response = self.client.post('/subtask/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)  
    
    def test_create_category(self):
        data = {
            "name": "Test Category",
            "color": "#FF0000"
        }
        
        response = self.client.post('/category/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)  
    
    
    def test_create_contact(self):
        data = {
            "name": "Test Contact",
            "phone": "1234567890",
            "email": "test@example.com",
            "acronym": "TC",
            "color": "#FF0000"
        }
        
        response = self.client.post('/contact/', data=json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 201) 
        
    
    def test_create_task(self):
        
        data = {
            "title": "Test Task",
            "description": "This is a test task description.",
            "category": 1,
            "assigned_to": [1],  
            "due_date": datetime.now().strftime("%Y-%m-%d"),  
            "prio": "High",  
            "column": "toDo",  
            "subtasks": []
        }
        response = self.client.post('/task/', data=json.dumps(data), content_type='application/json')
        print("Response status code:", response.data)
        self.assertEqual(response.status_code, 201)   
    
    
    def test_get_task(self):
        
        response = self.client.get('/task/')
        self.assertEqual(response.status_code, 200) 
    
    
    def test_get_contact(self):
        
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)  
    
    
    def test_get_category(self):
        
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)  
        
    
    def test_get_subtask(self):
        
        response = self.client.get('/subtask/')
        self.assertEqual(response.status_code, 200)  
        
    

    