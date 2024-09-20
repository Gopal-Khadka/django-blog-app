from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    # Token and Bearer are similar but "Bearer" is the specific implementation of "Token"
    # https://dev.to/satokenta/understanding-jwt-and-bearer-tokens-what-every-developer-should-know-35j8
    keyword = "Token"
