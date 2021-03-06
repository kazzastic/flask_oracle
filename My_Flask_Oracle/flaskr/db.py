#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 04:58:59 2019

@author: kazzastic
"""

import cx_Oracle
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        conn = cx_Oracle.connect("hr", "hr", "")
        g.db = conn.cursor()
        g.db.rowfactory
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
def init_db():
    db = get_db()
    db.execute('DROP TABLE usee cascade constraints')
    db.execute('DROP TABLE post')
    db.execute('CREATE TABLE usee(ID   INT              NOT NULL PRIMARY KEY,NAME VARCHAR (20)     NOT NULL,PASSWORD VARCHAR(10)  NOT NULL)')
    db.execute('CREATE TABLE post(id    INT              NOT NUll, author_id INT          NOT NULL,title VARCHAR(30)     NOT NULL,body VARCHAR(100)      NOT NULL,FOREIGN KEY(author_id) REFERENCES usee(id))')

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
    
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)