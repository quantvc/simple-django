from .common import *

INSTALLED_APPS += (
    "django_nose",
    "django_coverage",
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
