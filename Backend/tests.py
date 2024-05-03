from datetime import datetime
import json
import pdb
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from Backend.serializer import TaskPOSTSerializer

class TaskTest(APITestCase):    
    
    
    def setUp(self):
        self.username = 'testuser'
        self.email = 'test@example.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        
    
    #### TESTS SUBTASKS ####
    
    def test_create_subtask(self):
        data = {
            "name": "Test Subtask",
            "checked": False
        }
        
        
        response = self.client.post('/subtask/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)  
    
    
    def test_get_subtask(self):
        
        response = self.client.get('/subtask/')
        self.assertEqual(response.status_code, 200)
          
        
    def test_update_subtask(self):
        
        self.test_create_subtask()
        
        # Aktualisieren der Teilaufgabe
        updated_data = {
            "name": "Updated Subtask",
            "checked": True
        }
        
        response_update = self.client.put(f'/subtask/1/', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response_update.status_code, 200)
        self.assertEqual(response_update.json()['name'], updated_data['name'])
        self.assertEqual(response_update.json()['checked'], updated_data['checked'])
    
    def test_delete_subtask(self):
        
        self.test_create_subtask()        
        
        # Löschen der Teilaufgabe
        response_delete = self.client.delete(f'/subtask/1/')
        self.assertEqual(response_delete.status_code, 204)
        
        
        
        
    #### TEST CONTACTS ####
    
    def test_get_contact(self):
        
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200) 
        
    
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
        
        
    def test_update_contact(self):
        self.test_create_contact()
        
        updated_data = {
            "name": "Updated Contact",
            "phone": "0987654321",  
            "email": "updated@example.com",  
            "acronym": "UC",  
            "color": "#00FF00" 
        }
        response_update = self.client.put(f'/contact/1/', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response_update.status_code, 200)
        self.assertEqual(response_update.json()['name'], updated_data['name'])
        self.assertEqual(response_update.json()['phone'], updated_data['phone'])
        self.assertEqual(response_update.json()['email'], updated_data['email'])
        self.assertEqual(response_update.json()['acronym'], updated_data['acronym'])
        self.assertEqual(response_update.json()['color'], updated_data['color'])
        
        
    def test_delete_contact(self):
       
        self.test_create_contact()
        
        response_delete = self.client.delete(f'/contact/1/')
        self.assertEqual(response_delete.status_code, 204)
        
    
    #### TESTS CATEGORY #### 
    
    def test_create_category(self):
        data = {
            "name": "Test Category",
            "color": "#FF0000"
        }
        
        response = self.client.post('/category/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201) 
        
    
    def test_get_category(self):
        
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)  
        
        
    #### TESTS TASKS ####  
    
    
    def test_get_task(self):
        
        response = self.client.get('/task/')
        self.assertEqual(response.status_code, 200) 
        
        
    def test_create_task(self):
        
        self.test_create_contact()
        self.test_create_category()
        
        response_contact = self.client.get('/contact/')
        contact_id = response_contact.json()[0]['id']  # Annahme: Der erste erstellte Kontakt wird verwendet
        response_category = self.client.get('/category/')
        category_id = response_category.json()[0]['id'] 
        
        data = {
            "title": "Test Task",
            "description": "This is a test task description.",
            "category": category_id,
            "assigned_to": [contact_id],  
            "due_date": datetime.now().strftime("%Y-%m-%d"),  
            "prio": "High",  
            "column": "toDo",  
            "subtasks": []
        }       
        
        response = self.client.post('/task/', data=json.dumps(data), content_type='application/json')
        
        print("Response status code:", response.data)
        self.assertEqual(response.status_code, 201)   
    
    
     
    
    
      
        
    
      
        
    

    