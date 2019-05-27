#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:17:15 2019

@author: kazzastic
"""

from __future__ import print_function

import cx_Oracle

# Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
connection = cx_Oracle.connect("hr", "hr", "")

cursor = connection.cursor()
cursor.execute("""
    SELECT first_name
    FROM employees
    WHERE department_id = :did AND employee_id > :eid""",
    did = 50,
    eid = 190)
for fname in cursor:
    print("Values:", fname)