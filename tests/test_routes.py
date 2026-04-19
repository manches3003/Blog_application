import pytest
from app.models.blog_post import BlogPost


def test_index_route(client, app, db):
    with app.app_context():
        post = BlogPost(title='Test Post', content='Test content', author='Author')
        db.session.add(post)
        db.session.commit()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Test Post' in response.data


def test_view_post_route(client, app, db):
    with app.app_context():
        post = BlogPost(title='View Test', content='Content here', author='Author')
        db.session.add(post)
        db.session.commit()
        post_id = post.id
    response = client.get(f'/post/{post_id}')
    assert response.status_code == 200
    assert b'View Test' in response.data


def test_create_post_route_get(client):
    response = client.get('/create')
    assert response.status_code == 200
    assert b'Create New Post' in response.data


def test_create_post_route_post(client, app, db):
    response = client.post('/create', data={
        'title': 'New Post',
        'content': 'Post content',
        'author': 'Test Author'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'New Post' in response.data


def test_api_get_posts(client, app, db):
    with app.app_context():
        post = BlogPost(title='API Test', content='Content')
        db.session.add(post)
        db.session.commit()
    response = client.get('/api/posts')
    assert response.status_code == 200
    data = response.get_json()
    assert 'posts' in data
    assert len(data['posts']) > 0


def test_api_get_single_post(client, app, db):
    with app.app_context():
        post = BlogPost(title='API Single', content='Content')
        db.session.add(post)
        db.session.commit()
        post_id = post.id
    response = client.get(f'/api/posts/{post_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['post']['title'] == 'API Single'


def test_api_create_post(client, app):
    response = client.post('/api/posts', json={
        'title': 'API Created',
        'content': 'Created content',
        'author': 'API Author'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['post']['title'] == 'API Created'


def test_api_create_post_missing_fields(client):
    response = client.post('/api/posts', json={'title': 'Missing content'})
    assert response.status_code == 400
    assert b'error' in response.data


def test_api_nonexistent_post(client):
    response = client.get('/api/posts/99999')
    assert response.status_code == 404
