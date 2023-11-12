from django.views.generic import DetailView
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import WorkExperience


class WorkExperienceCreateViewSet(SnippetViewSet):
    icon = "desktop"
    menu_label = "Work Experience"
    menu_name = "Work Experience"
    menu_order = 100
    add_to_admin_menu = True