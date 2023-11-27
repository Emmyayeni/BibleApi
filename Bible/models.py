from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
import uuid

class Bible(models.Model):
    book = models.CharField(_("Book_Name"),max_length=255);
    book_number = models.IntegerField(_("Book_Number"))
    chapter = models.IntegerField(_("Chapter"))
    verse = models.IntegerField(_("Verse"))
    Text = models.TextField(_("Text"))

    def __str__(self):
        return f'{self.book} {self.chapter}:{self.verse}'
