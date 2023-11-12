from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from .blocks import PortfolioStreamBlock

class HomePage(Page):
    blocks = StreamField(
        PortfolioStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("blocks"),
    ]
