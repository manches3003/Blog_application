from flask import Blueprint, render_template
from app.models.blog_post import BlogPost
from app.routes.web import web_bp


@web_bp.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('index.html', posts=posts)


@web_bp.route('/post/<int:post_id>')
def view_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('post.html', post=post)
