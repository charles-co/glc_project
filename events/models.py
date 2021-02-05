from datetime import timedelta
from django.conf import settings
from django.db import models
from django.db.models import 
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

# Create your models here.
def images_directory_path(instance, filename):
        return '/'.join([str(instance.__class__.__name__.lower() + "_photos"), 
                        str(instance.__str__()),
                        str(uuid.uuid4().hex + ".jpg")])

