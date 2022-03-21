import datetime
from typing import TYPE_CHECKING, Iterable, Optional, Union
from uuid import uuid4

from django.conf import settings
from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.indexes import BTreeIndex, GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import JSONField  # type: ignore
from django.db.models import (
    BooleanField,
    Case,
    Count,
    DateField,
    Exists,
    ExpressionWrapper,
    F,
    FilteredRelation,
    OuterRef,
    Q,
    Subquery,
    Sum,
    TextField,
    Value,
    When,
)
from django.db.models.functions import Coalesce
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import smart_text
from versatileimagefield.fields import PPOIField, VersatileImageField


from .models import ModelWithMetadata, PublishableModel, SortableModel
from seo.models import SeoModel

# Create your models here.
class Category(ModelWithMetadata, SeoModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique=True, allow_unicode=True)
    description = models.TextField(blank=True, null=True)
    background_image = models.VersatileImageField(upload_to="media/images")
    background_image_alt = models.CharField(max_length=120, blank=True, null=True)
    
    