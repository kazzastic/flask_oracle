#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:47:44 2019

@author: kazzastic
"""
from __future__ import print_function
import os
import cx_Oracle
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        '''
        connection = cx_Oracle.connect("hr", "hr", "")
        cursor = connection.cursor()
        cursor.execute("""
            SELECT first_name
            FROM employees
            WHERE department_id = :did AND employee_id > :eid""",
            did = 50,
            eid = 190)
        for fname in cursor:
            return "Values:", fname
        '''
        return 'Hello, World!'

    return app