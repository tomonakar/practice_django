from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a User
        testuser1 = User.objects.create_user(
            username = 'testuser1',
            password = 'password123'
        )
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(
            author=testuser1,
            title='test_title',
            body='test_body'
        )
        test_post.save()

        def test_blog_content(self):
            post = Post.objects.get(id=1)
            expected_author = f'{post.author}'
            expected_title = f'{post.title}'
            expected_body = f'{post.body}'
            self.assertEquals(expected_author, 'testuser1')
            self.assertEquals(expected_title, 'test_title')
            self.assertEquals(expected_body, 'test_body')
