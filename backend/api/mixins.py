from rest_framework import permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .authentication import TokenAuthentication
from .permissions import IsAuthorPermission


class AuthorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsAuthorPermission]


class AuthenticationMixin:
    authentication_classes = [
        JWTAuthentication,
        TokenAuthentication,
        authentication.SessionAuthentication,
    ]
