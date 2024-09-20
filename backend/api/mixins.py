from rest_framework import permissions,authentication
from .authentication import TokenAuthentication
from .permissions import IsAuthorPermission


class AuthorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsAuthorPermission]


class AuthenticationMixin:
    authentication_classes = [TokenAuthentication, authentication.SessionAuthentication]