from django.test import TestCase
from . models import Category, Post
from django.contrib.auth.models import User

# Create your tests here.


class TestCreatePost(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='Django')
        test_user1 = User.objects.create(username='test_user1', password='123456789')
        test_post = Post.objects.create(category_id=1, title='Django', excerpt='in this tutorial...',
                                        content='in this tutorial...', slug='django', author_id=1,
                                        status='published')

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        status = f'{post.status}'
        author = f'{post.author}'
        title = f'{post.title}'
        slug = f'{post.slug}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(excerpt, 'in this tutorial...')
        self.assertEqual(content, 'in this tutorial...')
        self.assertEqual(status, 'published')
        self.assertEqual(title, 'Django')
        self.assertEqual(slug, 'django')
        self.assertEqual(str(post), 'Django')
        self.assertEqual(str(cat), 'Django')
