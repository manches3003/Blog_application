from flask import Blueprint, jsonify, request
from app import db
from app.models.blog_post import BlogPost
from app.routes.api import api_bp


@api_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'title and content are required'}), 400

    post = BlogPost(
        title=data['title'],
        content=data['content'],
        author=data.get('author', 'Anonymous')
    )
    db.session.add(post)
    db.session.commit()

    return jsonify({'post': post.to_dict()}), 201
