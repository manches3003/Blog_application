import pytest
from app.models.blog_post import BlogPost


def test_create_post(app, db):
    with app.app_context():
        post = BlogPost(title='Test', content='Test content', author='Test Author')
        db.session.add(post)
        db.session.commit()
        assert post.id is not None
        assert post.title == 'Test'


def test_post_to_dict(app, db):
    with app.app_context():
        post = BlogPost(title='Test', content='Test content', author='Author')
        db.session.add(post)
        db.session.commit()
        data = post.to_dict()
        assert data['title'] == 'Test'
        assert data['content'] == 'Test content'
        assert data['author'] == 'Author'
        assert 'created_at' in data


def test_post_default_author(app, db):
    with app.app_context():
        post = BlogPost(title='Test', content='Content')
        db.session.add(post)
        db.session.commit()
        assert post.author == 'Anonymous'


def test_post_timestamps(app, db):
    with app.app_context():
        post = BlogPost(title='Test', content='Content')
        db.session.add(post)
        db.session.commit()
        assert post.created_at is not None
        assert post.updated_at is not None
