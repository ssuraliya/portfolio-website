from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.fields import RichTextField

from .blocks import PortfolioStreamBlock

class HomePage(Page):
    blocks = StreamField(
        PortfolioStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("blocks"),
    ]


class WorkExperience(models.Model):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True, default=None, blank=True)
    position = models.CharField(max_length=255, null=False, blank=False)
    company_name = models.CharField(max_length=255, null=False, blank=False)
    description = RichTextField(null=False)
    skills = models.TextField(null=True, help_text="Comma separated skills")
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    content_panels = [
        FieldPanel("start_date"),
        FieldPanel("end_date"),
        FieldPanel("position"),
        FieldPanel("company_name"),
        FieldPanel("description"),
    ]

    @property
    def start(self):
        return self.start_date.strftime("%B, %Y")

    @property
    def end(self):
        if self.end_date:
            return self.end_date.strftime("%B, %Y")
        return 'Present'


    @property
    def skills_list(self):
        if not self.skills:
            return []
        
        return list(map(str.strip, self.skills.split(',')))
