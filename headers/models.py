"""Menus models."""
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.db.transaction import atomic
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, PageChooserPanel
from wagtail.models import Orderable, PreviewableMixin


from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

class HeaderItem(Orderable):
    link_title = models.CharField(blank=True, null=True, max_length=50)
    link_url = models.CharField(max_length=500, blank=True)
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    header = ParentalKey("Header", related_name="header_items")
    block_id = models.CharField(
        max_length=255, blank=True, null=True, help_text="ID of internal blocks of page."
    )

    panels = [
        FieldPanel("link_title"),
        FieldRowPanel(
            children=(
                FieldPanel("link_url"),
                PageChooserPanel("link_page"),
            ),
            heading="Page Selection",
        ),
        FieldPanel("block_id"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        url = "#"
        if self.link_page:
            url = self.link_page.url
        elif self.link_url:
            url = self.link_url
        else:
            return "#"
        if self.block_id:
            return f"{url}#{self.block_id}"
        return url

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing Title"

    def clean(self) -> None:
        if self.link_url and self.link_page:
            raise DjangoValidationError("Select either page or enter link url")

@register_setting(icon='bars')
class Header(PreviewableMixin, BaseGenericSetting, ClusterableModel):
    class Meta:
        verbose_name = "Header for the site"

    panels = [
        InlinePanel("header_items", label="Header Item"),
    ]


    def get_preview_template(self, request, mode_name):
        return "headers/preview/header.html"
