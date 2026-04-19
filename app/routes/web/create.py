from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models.blog_post import BlogPost
from app.routes.web import web_bp


@web_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        post = BlogPost(
            title=request.form.get('title'),
            content=request.form.get('content'),
            author=request.form.get('author', 'Anonymous')
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully', 'success')
        return redirect(url_for('web.view_post', post_id=post.id))
    return render_template('create.html')
