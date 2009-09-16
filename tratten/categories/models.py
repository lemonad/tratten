from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CategoryManager(models.Manager):
    pass


class Category(models.Model):
    """An issue category.

    >>> c = Category(name="Hardware")
    >>> c.save()

    """

    name = models.CharField(_("Name"),
                            unique=True,
                            db_index=True,
                            max_length=100)
    created_at = models.DateTimeField(_("Created"),
                                      db_index=True,
                                      auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed"),
                                      db_index=True,
                                      auto_now=True)
    objects = CategoryManager()


    class Meta:
        ordering = ['name']
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __unicode__(self):
        return self.name
