from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from blogs.models import BlogPost, BlogAuthor

User = get_user_model()


class BlogAPITest(APITestCase):

    def setUp(self):
        # create user and its author with token

        self.user = User.objects.create_superuser(
            username="testuser", password="testpass"
        )
        self.blog_author = BlogAuthor.objects.create(user=self.user, bio="Author bio")
        self.token = Token.objects.create(user=self.user)

        self.blog_data = {
            "title": "Test Blog",
            "content": "This is a test blog content.",
            "author_id": self.blog_author.pk,
        }
        self.blog = BlogPost.objects.create(**self.blog_data)
        self.blog_create_url = reverse("blog-create")
        self.blog_list_url = reverse("blog-list")
        self.blog_detail_url = reverse("blog-detail", args=[self.blog.slug])
        self.blog_delete_url = reverse("blog-delete", args=[self.blog.slug])
        self.blog_update_url = reverse("blog-edit", args=[self.blog.slug])

        self.add_user_permissions()

    def authenticate(self):
        """
        Authenticate the client with the token generated for the user in setup.

        This is used in each test method to authenticate the client before making
        the request. The authentication token is added to the headers of the
        request using the `credentials` attribute of the APIClient.
        """
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def create_permissions(self):
        """
        Create the required permissions for the BlogPost model.

        This method creates the permissions required by the permission mixins
        used in the BlogPost API views. The permissions created are:

        - can_add_blogpost: Can add blog post
        - can_view_blogpost: Can view blog post
        - can_change_blogpost: Can change blog post
        - can_delete_blogpost: Can delete blog post
        """
        content_type = ContentType.objects.get_for_model(BlogPost)

        permissions = [
            ("can_add_blogpost", "Can add blog post"),
            ("can_view_blogpost", "Can view blog post"),
            ("can_change_blogpost", "Can change blog post"),
            ("can_delete_blogpost", "Can delete blog post"),
        ]

        for codename, name in permissions:
            Permission.objects.get_or_create(
                codename=codename, name=name, content_type=content_type
            )

    def add_user_permissions(self):
        """
        Add required permissions to the user created in setup.

        This method creates the required permissions for the BlogPost model
        using the create_permissions method. It then adds the created permissions
        to the user created in setup to handle permission mixins used in the
        BlogPost API views.
        """
        self.create_permissions()  # create required permissions

        # add permissions to user to handle permission mixins
        self.add_permission = Permission.objects.get(codename="can_add_blogpost")
        self.view_permission = Permission.objects.get(codename="can_view_blogpost")
        self.change_permission = Permission.objects.get(codename="can_change_blogpost")
        self.delete_permission = Permission.objects.get(codename="can_delete_blogpost")

        self.user.user_permissions.add(self.add_permission)
        self.user.user_permissions.add(self.view_permission)
        self.user.user_permissions.add(self.change_permission)
        self.user.user_permissions.add(self.delete_permission)

    def test_create_blog(self):
        self.authenticate()
        response = self.client.post(self.blog_create_url, self.blog_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)  # Ensure one blog is created
        self.assertEqual(BlogPost.objects.last().title, "Test Blog")

    def test_list_blog(self):
        self.authenticate()
        response = self.client.get(self.blog_list_url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].get("title"), self.blog.title)

    def test_detail_blog(self):
        self.authenticate()
        response = self.client.get(self.blog_detail_url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.blog.title)

    def test_update_blog(self):
        self.authenticate()
        updated_blog = self.blog_data.copy()
        updated_blog.update({"title": "New test title"})
        response = self.client.put(self.blog_update_url, updated_blog)

        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), updated_blog.get("title"))

        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, updated_blog.get("title"))

    def test_delete_blog(self):
        self.authenticate()
        response = self.client.delete(self.blog_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(), 0)
