#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:59:39 2019

@author: kazzastic
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import cx_Oracle
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, author_id, name FROM post p JOIN usee u ON p.author_id = u.id ORDER BY p.id DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        conn = cx_Oracle.connect("hr", "hr", "")

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (id , author_id, title, body) VALUES (:id,:author_id, :title, :body)',
                {"id":'2',"author_id":'1', "title":title, "body":body})
            conn.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, author_id, title, body, name'
        ' FROM post p JOIN usee u ON p.author_id = u.id'
        ' WHERE p.id = :id',
        {"id":id}
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    #if check_author and post[4] != g.user[0]:
     #   abort(403)

    return post
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        conn = cx_Oracle.connect("hr", "hr", "")
        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = :title, body = :body'
                ' WHERE id = :id',
                {"title":title, "body":body, "id":id}
            )
            conn.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    conn = cx_Oracle.connect("hr", "hr", "")
    db = get_db()
    db.execute('DELETE FROM post WHERE id = :id', {"id":id})
    conn.commit()
    return redirect(url_for('blog.index'))