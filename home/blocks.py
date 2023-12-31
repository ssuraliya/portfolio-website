from wagtail import blocks
from wagtail.snippets.blocks import SnippetChooserBlock


class BaseStructBlock(blocks.StructBlock):
    id = blocks.CharBlock(
        null=True,
        required=False,
        help_text="ID of this block. Can be used to link the block in header",
    )


class NameSection(BaseStructBlock):
    name = blocks.CharBlock(required=True)
    position = blocks.CharBlock(required=True)
    company_name = blocks.CharBlock(required=True)
    contact_no = blocks.CharBlock(required=True)
    email = blocks.CharBlock(required=True)
    location = blocks.CharBlock(required=True)
    
    class Meta:
        template = "blocks/name_section.html"
        
class AboutMeSection(BaseStructBlock):
    content = blocks.RichTextBlock(required=True)

    class Meta:
        template = "blocks/about_me.html"

class Skills(BaseStructBlock):
    skill_groups = blocks.ListBlock(SnippetChooserBlock('home.SkillGroup'))
    
    class Meta:
        template = "blocks/skills.html"

class WorkExperienceSection(BaseStructBlock):
    works = blocks.ListBlock(SnippetChooserBlock('home.WorkExperience'))

    class Meta:
        template = "blocks/work_experience.html"
        icon = "desktop"

class ProjectSelection(BaseStructBlock):
    projects = blocks.ListBlock(SnippetChooserBlock('home.Project'))

    class Meta:
        template = "blocks/project.html"
        icon = 'code'


class PortfolioStreamBlock(blocks.StreamBlock):
    name_section = NameSection()
    about_me = AboutMeSection()
    work_experience = WorkExperienceSection()
    projects = ProjectSelection()
    skills = Skills()
