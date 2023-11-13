from wagtail.snippets.models import register_snippet

from .models import WorkExperience, Project
from .viewsets import WorkExperienceCreateViewSet, ProjectsCreateViewSet

register_snippet(WorkExperience, viewset=WorkExperienceCreateViewSet)
register_snippet(Project, viewset=ProjectsCreateViewSet)