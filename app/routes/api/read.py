from flask import jsonify
from app import db
from app.models.blog_post import BlogPost
from app.routes.api import api_bp


@api_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return jsonify({'posts': [p.to_dict() for p in posts]})


@api_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return jsonify({'post': post.to_dict()})
