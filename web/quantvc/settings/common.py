# encoding:utf-8

from .base import *


# userea
AUTH_PROFILE_MODULE = "accounts.Profile"
USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

# django guardian
ANONYMOUS_USER_ID = -1