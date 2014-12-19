from django.db import models

from django.utils.translation import ugettext_lazy as _

from userena.models import UserenaLanguageBaseProfile
from userena.utils import user_model_label


class Profile(UserenaLanguageBaseProfile):
    """ Default profile """
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
    )
    user = models.OneToOneField(user_model_label, unique=True, verbose_name=_('user'), related_name='profile')
    gender = models.PositiveSmallIntegerField(verbose_name=_('gender'), choices=GENDER_CHOICES, blank=True, null=True)
    birth_date = models.DateField(verbose_name=_('birth date'), blank=True, null=True)
    about_me = models.TextField(verbose_name=_('about me'), blank=True)