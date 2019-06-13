from unittest import TestCase
from ccfunctions import *

class TestFunc(TestCase):
    def test_is_string(self):
        a = ccypher.superEncrypt()
        self.assertTrue(isinstance(a, basestring))
        b = ccypher.encryptor()
        self.assertTrue(isinstance(b, basestring))
        
