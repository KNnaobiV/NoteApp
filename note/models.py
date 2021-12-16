from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Note(models.Model):
    author = models.ManyToManyField(CustomUser)
    title = models.CharField(null=False, blank=False, max_length=255)
    body = models.TextField(null=False, blank=False)
    slug = models.SlugField(max_length=255)
    PUBLISH_STATUS = (
            ('draft', 'DRAFT'), ('published', 'PUBLISHED'),
            )
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=PUBLISH_STATUS,
            default='draft')

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('note:note-detail',
                args=[self.pk, self.slug])
