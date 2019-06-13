from unittest import TestCase
from ccypher import *

class TestFunc(TestCase):
    def test_is_string(self):
        a = ccypher.clickRun()
        self.assertTrue(isinstance(a, basestring))
        b = ccypher.buttonConfig()
        self.assertTrue(isinstance(b, basestring))
        c = ccypher.copyOut()
        self.assertTrue(isinstance(c, basestring))
        d = ccypher.clearInBox()
        self.assertTrue(isinstance(d, basestring))
        e = ccypher.clearOutBox()
        self.assertTrue(isinstance(e, basestring))
        f = ccypher.copySel()
        self.assertTrue(isinstance(f, basestring))
        g = ccypher.pasteSel()
        self.assertTrue(isinstance(g, basestring))
        h = ccypher.close_window()
        self.assertTrue(isinstance(h, basestring))
        
        
