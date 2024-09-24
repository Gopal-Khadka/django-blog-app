from rest_framework import permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .authentication import TokenAuthentication
from .permissions import IsAuthorPermission,IsAuthorOrAdminUser


class AuthorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsAuthorPermission]


class ForumCreatePermissionMixin:
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    
class ForumUpdatePermissionMixin:
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrAdminUser]


class ForumPermissionMixin:
    permission_classes = [permissions.IsAuthenticated]


class AuthenticationMixin:
    authentication_classes = [
        JWTAuthentication,
        TokenAuthentication,
        authentication.SessionAuthentication,
    ]
