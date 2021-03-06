from django.test import TestCase
from items.models import Item
from user.models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Model
import os
from django.core.serializers import serialize


from myutils.query_utils import query_to_json, get_field_names
# Create your tests here.

# Query to JSON test
class JSONTestCase(TestCase):
    # Create users and 2 listings per user
    def setUp(self):
        item_id = 1
        for i in range(1, 2):
            index = str(i)
            user = User.objects.create_user('testusername'+index, 'testemail'+index, 'testpassword'+index,date_joined="2020-04-22 00:00:01")
            profile = UserProfile.objects.create(user=user, phone='testphone'+index)
            item = Item.objects.create(
                item_id = item_id,
                name = 'Item'+str(item_id),
                seller = profile,
                description ='Description'+str(item_id),
                price=item_id,
                quantity=item_id,
                date_uploaded="04/22/2020"
            )
            item_id += 1
            item2 = Item.objects.create(
                item_id=item_id,
                name='Item' + str(item_id),
                seller=profile,
                description='Description' + str(item_id),
                price=item_id,
                quantity=item_id,
                date_uploaded="2020-04-22"
            )
          #  item_id += 1



    def test_query_to_json(self):
        items = Item.objects.all()
        item_json = query_to_json(items, exclude_fields="password")
        expected_json = open(os.path.join(os.path.dirname(__file__), 'test_files/test_query_to_json_expected.txt'))
        expected_json = expected_json.read()
        self.assertEquals(item_json, expected_json)
    
    #def searchByCategory 

#class ItemTestCase(TestCase):
 #   def setUp(self):
        


   

