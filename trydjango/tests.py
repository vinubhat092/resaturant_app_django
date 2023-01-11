from django.test import TestCase
import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
class trydjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        self.assertNotIn(SECRET_KEY,'abc')
        
        try:
            is_strong = validate_password(SECRET_KEY)  #to check wether password is strong enough
        except Exception as e:
            msg = f'Weak Secret Key  {e.messages}'
            self.fail(msg)