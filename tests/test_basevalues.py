#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author:
# Linwood Creekmore
# Email: valinvescap@gmail.com

##############################
# Standard Library Import
##############################

import os
from unittest import TestCase

import numpy as np
import pandas as pd

##############################
# Custom Library Import
##############################
#
import gdelt
from gdelt.base import codes, BASE_DIR


##############################
# Third Party Libraries
##############################

class TestBaseValues(TestCase):
    def test_codedataframe(self):
        """Test install data"""

        f = os.path.join(BASE_DIR, 'data', 'cameoCodes.json')
        resp = pd.read_json(f,dtype={'cameoCode': 'str', "GoldsteinScale": np.float64})
        resp.set_index('cameoCode', drop=False, inplace=True)
        print("This is {}".format(gdelt.__file__))
        return (self.assertTrue(resp.equals(codes)))

    def test_proxy_dict(self):
        "Test if proxy is dictionary"

        proxies = {"http": None, "https": None}
        gd = gdelt.gdelt(proxies=proxies)
        self.assertTrue(isinstance(gd.proxies, dict), "Test for dictonary not "
                                                      "working.")

    def test_proxy_dict_fail(self):
        exp = ("The proxies parameter must be a dictionary. See http://docs."
               "python-requests.org/en/master/user/advanced/#proxies for "
               "more information.")
        with self.assertRaises(Exception) as context:
            gd = gdelt.gdelt(proxies="nope")
        the_exception = context.exception
        return self.assertEqual(exp, str(the_exception), "The proxy dictionary"
                                                         " error failed.")
