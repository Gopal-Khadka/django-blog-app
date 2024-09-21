from uuid import UUID
from django.test import TestCase
from django.contrib.auth import get_user_model
from blogs.models import BlogPost, BlogAuthor, Tag, Comment, Like, Contact

User = get_user_model()


class BlogModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
            first_name="Test",
            last_name="User",
        )
        self.blog_author = BlogAuthor.objects.create(user=self.user)
        self.tag = Tag.objects.create(name="Django")
        self.blog_data = {
            "author": self.blog_author,
            "title": "Test Blog Post",
            "content": "Content of test blog",
        }
        self.blog_post = BlogPost.objects.create(**self.blog_data)

    def test_blog_author_creation(self):
        self.blog_author.name = "Writer OP"
        self.blog_author.save()

        self.assertEqual(self.blog_author.user.username, "testuser")
        self.assertEqual(str(self.user.username), "testuser")
        self.assertEqual(str(self.blog_author.name), "Writer OP")

    def test_blog_author_name_validation(self):
        self.assertEqual(self.user.get_full_name(), self.blog_author.name)

    def test_blog_post_creation(self):
        self.assertEqual(self.blog_post.author, self.blog_author)
        self.assertEqual(self.blog_post.title, self.blog_data["title"])

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Python")
        self.assertEqual(tag.name, "Python")
        self.assertEqual(str(tag), "Python")

    def test_blog_post_uuid_generation(self):
        self.assertIsNotNone(str(self.blog_post.unique_id))
        self.assertIsInstance(self.blog_post.unique_id, UUID)

    def test_blog_post_slug_generation(self):
        self.assertIsNotNone(self.blog_post.slug)
        self.assertIn(str(self.blog_post.unique_id)[:6], self.blog_post.slug)

    def test_get_tags_list(self):
        self.blog_post.tags.add(self.tag)
        self.assertIn(self.tag.name, self.blog_post.get_tags_list())

    def test_blog_post_string_representation(self):
        expected_str = f"{self.blog_post.title} - {self.blog_author.name}"
        self.assertEqual(str(self.blog_post), expected_str)

    def test_comment_creation(self):
        comment = Comment.objects.create(
            post=self.blog_post, author=self.blog_author.user, content="New comment"
        )
        self.assertEqual(comment.post, self.blog_post)
        self.assertEqual(comment.author, self.blog_author.user)
        self.assertEqual(comment.content, "New comment")

    def test_like_creation(self):
        like = Like.objects.create(post=self.blog_post, author=self.blog_author.user)
        self.assertEqual(like.post, self.blog_post)
        self.assertEqual(like.author, self.blog_author.user)

    def test_contact_creation(self):
        contact = Contact.objects.create(
            name="Contact User",
            email="test@example.com",
            message="Random message",
        )
        self.assertEqual(contact.name, "Contact User")
        self.assertEqual(contact.email, "test@example.com")
        self.assertEqual(contact.message, "Random message")
