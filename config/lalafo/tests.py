from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from .models import Ad

class AdCreateTestCase(TestCase):
    def test_create_ad(self):
       
        ad_data = {
            'title': 'Test Ad',
            'description': 'This is a test ad.',
            'price': 100.0,
            'city': 'Test City',
            'category': 'Test Category',
            'photos': ['photo1.jpg', 'photo2.jpg'],
            'phone': '123-456-7890',
            'author': 'Test Author',
        }

        response = self.client.post(reverse('create_ad'), ad_data)

        self.assertEqual(response.status_code, 302)

        
        self.assertEqual(Ad.objects.count(), 1)

        
        created_ad = Ad.objects.first()

     
        self.assertEqual(created_ad.title, ad_data['title'])
        self.assertEqual(created_ad.description, ad_data['description'])
        self.assertEqual(created_ad.price, ad_data['price'])
        self.assertEqual(created_ad.city, ad_data['city'])
        self.assertEqual(created_ad.category, ad_data['category'])
        self.assertEqual(created_ad.photos, ad_data['photos'])
        self.assertEqual(created_ad.phone, ad_data['phone'])
        self.assertEqual(created_ad.author, ad_data['author'])
