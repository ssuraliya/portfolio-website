from wagtail.snippets.models import register_snippet

from .models import WorkExperience, Project, SkillGroup
from .viewsets import WorkExperienceCreateViewSet, ProjectsCreateViewSet, SkillGroupCreateViewSet

register_snippet(WorkExperience, viewset=WorkExperienceCreateViewSet)
register_snippet(Project, viewset=ProjectsCreateViewSet)
register_snippet(SkillGroup, viewset=SkillGroupCreateViewSet)