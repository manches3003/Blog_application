from flask import Blueprint, redirect, url_for, flash
from app import db
from app.models.blog_post import BlogPost
from app.routes.web import web_bp


@web_bp.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully', 'success')
    return redirect(url_for('web.index'))
