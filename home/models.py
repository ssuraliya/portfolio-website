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

    def __str__(self) -> str:
        return f'{self.position}: {self.company_name}'

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


class Project(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = RichTextField(null=False)
    skills = models.TextField(null=True, help_text="Comma separated skills")
    code_link = models.URLField(null=True, blank=True)
    report_link  = models.URLField(null=True, blank=True)
    live_link = models.URLField(null=True, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    content_panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("skills"),
        FieldPanel("code_link"),
        FieldPanel("report_link"),
        FieldPanel("live_link"),
    ]
    
    def __str__(self) -> str:
        return self.title

    @property
    def skills_list(self):
        if not self.skills:
            return []
        
        return list(map(str.strip, self.skills.split(',')))

