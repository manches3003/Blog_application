from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models.blog_post import BlogPost
from app.routes.web import web_bp


@web_bp.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title', post.title)
        post.content = request.form.get('content', post.content)
        post.author = request.form.get('author', post.author)
        db.session.commit()
        flash('Post updated successfully', 'success')
        return redirect(url_for('web.view_post', post_id=post.id))
    return render_template('edit.html', post=post)
