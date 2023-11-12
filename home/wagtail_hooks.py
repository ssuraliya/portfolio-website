from wagtail.snippets.models import register_snippet

from .models import WorkExperience
from .viewsets import WorkExperienceCreateViewSet

register_snippet(WorkExperience, viewset=WorkExperienceCreateViewSet)