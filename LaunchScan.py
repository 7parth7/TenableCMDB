# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:22:29 2020

@author: pkb13
"""

import os
import requests,json
from tenable.sc import TenableSC

USER = os.environ.get("TenableUser")
PASS = os.environ.get("TenablePassword")


# Login to Tenable.sc
sc = TenableSC('tenable.partners.org')
sc.login(USER , PASS)

running = sc.scans.launch(1924)
print(running)