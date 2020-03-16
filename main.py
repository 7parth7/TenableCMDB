# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:22:29 2020

@author: pkb13
"""

import os
import requests,json
from tenable.sc import TenableSC
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
key = key.decode()
print(key)
cipher_suite = Fernet(key)
print (cipher_suite)




USER = os.environ.get("TenableUser")
PASS = os.environ.get("TenablePassword")
encrypted = cipher_suite.encrypt(PASS.encode())
print(encrypted)

# Login to Tenable.sc
# sc = TenableSC('tenable.partners.org')
# sc.login(USER , PASS)

